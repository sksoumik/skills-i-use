#!/usr/bin/env python3
"""Print a Claude Code session transcript as a short dialogue, for /distill.

Usage:
  extract_session.py <transcript.jsonl>   print the dialogue
  extract_session.py --find current       path of the session whose last human turn is /distill
  extract_session.py --find today         paths of sessions changed today, in every project
  extract_session.py --find <session-id>  path of that session
"""
import datetime
import glob
import json
import os
import re
import sys

PROJECTS = os.path.expanduser("~/.claude/projects")
DISTILL_CALL = "<command-name>/distill</command-name>"
REMINDER = re.compile(r"<system-reminder>.*?</system-reminder>", re.S)
MAX_HUMAN = 3000  # pasted logs can be huge; the start is enough to see the point
MAX_ERROR = 300
MAX_LINE = 1500  # keep lines short enough for the Read tool


def is_mid_turn_message(d):
    """A message the person typed while the agent was still working.

    These are saved as attachments, not user records, and they are often corrections.
    Background task notices use the same attachment type with another commandMode.
    """
    a = d.get("attachment")
    return isinstance(a, dict) and a.get("type") == "queued_command" and a.get("commandMode") == "prompt"


def records(path):
    """Main-thread user, assistant and mid-turn message records. Subagent records are skipped."""
    with open(path) as fh:
        for line in fh:
            try:
                d = json.loads(line)
            except json.JSONDecodeError:
                continue
            if d.get("isSidechain"):
                continue
            if d.get("type") in ("user", "assistant") or is_mid_turn_message(d):
                yield d


def blocks(d):
    c = d["attachment"]["prompt"] if is_mid_turn_message(d) else d["message"]["content"]
    return [{"type": "text", "text": c}] if isinstance(c, str) else c


def human_text(d):
    """Text a person typed, or None for tool results, skill bodies and compact summaries.

    Compact summaries are skipped because the messages they summarise are still
    earlier in the same file.
    """
    if not is_mid_turn_message(d) and (d["type"] != "user" or d.get("isMeta") or d.get("isCompactSummary")):
        return None
    parts = [b["text"] for b in blocks(d) if b.get("type") == "text"]
    text = REMINDER.sub("", "\n".join(parts)).strip()
    return text or None


def one_line(value, limit):
    return " ".join(str(value).split())[:limit]


def tool_line(b):
    inp = b.get("input") or {}
    hint = next((inp[k] for k in ("description", "file_path", "command", "query", "prompt") if inp.get(k)), "")
    return f"  [{b.get('name')}] {one_line(hint, 150)}"


def error_text(b):
    c = b.get("content")
    if isinstance(c, list):
        c = " ".join(x.get("text", "") for x in c if isinstance(x, dict))
    return one_line(c, MAX_ERROR)


def split_long(line):
    while len(line) > MAX_LINE:
        cut = line.rfind(" ", 0, MAX_LINE)
        cut = cut if cut > 0 else MAX_LINE
        yield line[:cut]
        line = line[cut:].lstrip()
    yield line


def print_dialogue(path):
    out, turn, first, last = [], 0, None, None
    for d in records(path):
        ts = d.get("timestamp", "")[:16].replace("T", " ")
        first, last = first or ts, ts or last
        human = human_text(d)
        if human is not None:
            turn += 1
            if len(human) > MAX_HUMAN:
                human = human[:MAX_HUMAN] + f" [... {len(human) - MAX_HUMAN} chars cut]"
            label = "USER (typed while you worked)" if is_mid_turn_message(d) else "USER"
            out.append(f"\n=== T{turn} | {ts} UTC ===\n{label}: {human}")
            continue
        for b in blocks(d):
            kind = b.get("type")
            if d["type"] == "assistant" and kind == "text" and b["text"].strip():
                out.append(f"CLAUDE: {b['text'].strip()}")
            elif kind == "tool_use":
                out.append(tool_line(b))
            elif kind == "tool_result" and b.get("is_error"):
                out.append(f"  [error] {error_text(b)}")
    session_id = os.path.basename(path)[: -len(".jsonl")]
    print(f"session {session_id} | {first} to {last} UTC | {turn} human turns")
    for chunk in out:
        for line in chunk.split("\n"):
            print("\n".join(split_long(line)))


def human_turns(path):
    return [h for h in map(human_text, records(path)) if h is not None]


def find(what):
    files = sorted(glob.glob(os.path.join(PROJECTS, "*", "*.jsonl")), key=os.path.getmtime, reverse=True)
    if what == "current":
        for path in files[:20]:
            turns = human_turns(path)
            if turns and DISTILL_CALL in turns[-1]:
                return [path]
        return []
    if what == "today":
        midnight = datetime.datetime.combine(datetime.date.today(), datetime.time()).timestamp()
        # A session whose only turn is the /distill call has nothing to learn from.
        return [p for p in files if os.path.getmtime(p) >= midnight and len(human_turns(p)) >= 2]
    return [p for p in files if os.path.basename(p) == f"{what}.jsonl"]


def main(argv):
    if len(argv) == 3 and argv[1] == "--find":
        paths = find(argv[2])
        if not paths:
            print("no session found", file=sys.stderr)
            return 1
        print("\n".join(paths))
        return 0
    if len(argv) == 2 and os.path.isfile(argv[1]):
        print_dialogue(argv[1])
        return 0
    print(__doc__, file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
