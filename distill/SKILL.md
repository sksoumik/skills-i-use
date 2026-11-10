---
name: distill
description: Turn work sessions into general lessons I can use at any company.
disable-model-invocation: true
argument-hint: "[blank = this session | today | session id]"
---

The user solved specific problems with you. Now they want the **lessons** under those fixes, written so that they learn the concepts and can use them at another company, for example in a meeting about a different project.

Each lesson is a short article that teaches. A reader who never saw this project opens the file months later and understands three things: the situation, the terms, and the options. The situation is told in general words, without the codebase. The terms are explained: what each one is, why people use it, and when to use it. The options are what we did, and what else could work.

## 1. Read the whole source

Read the session transcripts on disk, not only your context window. Compaction drops detail, and the dropped detail often holds the lesson.

The helper is `~/.claude/skills/distill/extract_session.py`.

- Find the files: `python3 <helper> --find current` when there is no argument, `--find today` for `today`, or `--find <session-id>` for a session id.
- Read each file: `python3 <helper> <file> > /tmp/distill-<session-id>.txt`, then read that text file in parts. It holds the human turns with numbers, your text replies, tool names, and tool errors. It drops tool output, which is most of the transcript.
- One session fits in context. For several sessions, give each session to its own subagent. Tell it to read this skill, do steps 1 to 3 for that one session, and return each lesson with its facts: the situation, the cause, what was done, and the result.

Done when every human turn in the source has been read. Sampling is not reading.

## 2. Find the turning points

A turning point is a moment where someone's understanding changed. Scan for these kinds:

- **Surprise**: a result went against what someone expected.
- **Correction**: the user corrected you, you corrected yourself, or a conclusion was withdrawn.
- **Dead end**: an approach was tried and dropped.
- **Hidden cause**: the real cause of a bug or a bad number sat far from where it showed, and some check exposed it.
- **Tradeoff**: a choice between options, and the reason one won.
- **Hindsight shortcut**: a step that would have saved hours if done first.
- **Friction**: the user repeated a request, pushed back, or showed frustration.

Routine work, where a command ran and worked, is not a turning point.

Done when every surprise, correction, withdrawn conclusion, and dropped approach in the source is on the list.

## 3. Find the general idea

For each turning point, ask: what general idea solved this, or would have prevented it? When engineers have a common name for the idea, such as data leakage or regression test, use that name.

Merge turning points that lead to the same idea.

Done when every turning point has a general idea or is merged into one.

## 4. Filter

Keep a lesson only when it passes all three tests:

- **Portable**: the idea helps at another company, on another project.
- **Non-obvious**: a senior engineer does not already do it by default. "Test your code" fails. "Check every input of an example for test data, not only the example" passes.
- **Useful**: it changes what the reader does next time.

Keep the best 3 to 7. When nothing passes, report that; a session with no lesson is a valid result.

## 5. Write the lessons

Folder: `~/learning-journal/`. Each file holds one topic, like a chapter in a book.

- Topic: the subject the lessons teach, in 3 to 8 words. Example: "Techniques to Fine-Tune an SFT Model".
- File name: the topic in lowercase with hyphens, for example `techniques-to-fine-tune-an-sft-model.md`.
- Read the existing file titles first. Put each lesson in the file whose topic fits it. Create a new file only for a new topic.
- Each file starts with front matter `sessions: [<session ids>]`. When the same lesson already exists, improve it only if this session adds something new. On a second run over the same session, update its lessons in place.

Each lesson uses these parts, in this order:

1. `## <title>`: the idea in plain words.
2. `### The situation`: what we were doing and what went wrong or what we needed. Tell it in general words, so that a stranger can follow: "a grading service", "a partner company", "an open model". Leave out the codebase: no file, function, ticket, product, company, or person names. Use a rough size, such as "hundreds of runs" or "about half", only when the size helps the reader.
3. `### Terms you need`: one to three terms that the reader must know. For each term, say what it is, why people use it, and when to use it.
4. `### Why it happened`: the cause, step by step.
5. `### What we did`: what we tried and what worked, as ideas, not as code.
6. `### Other ways to solve it`: two to four other approaches from general practice, not only from the session. For each, say how it works, when it is a good choice, and its weak point.
7. `### The lesson`: one to three sentences to remember.

When a part does not fit a lesson, for example a lesson with no failure has no "Why it happened", leave that part out.

A good lesson looks like this:

```markdown
## Change the old answers the same way, then compare

### The situation

We had a grading service. It gives each run of an AI agent a score from 0 to 100. One rule took points away when the agent used more tool calls than it needed. We decided to remove this rule.

The project had a safety rule. Every change to the grading code must pass a regression test before review. This test grades hundreds of old runs again. Each new score must be exactly the same as the saved score.

Our change made many scores go up on purpose. So the test would fail, even with correct code.

### Terms you need

**Regression test.** A regression is a bug that breaks something that worked before. A regression test runs old cases again and compares the results with saved results. People use it to catch changes that they did not plan. Use it when many people or systems depend on the output. Examples are a grader, a billing system, or a report.

**Reference results.** These are the saved results that a regression test compares against. They show what "correct" was before the change. People also call them golden results.

### Why it happened

A regression test can only say "same" or "different". It cannot tell a planned change from a mistake. So a change on purpose fails the test on every case that it touches.

### What we did

We wrote a small function that applies only the planned change to the saved results. It removed the old penalty points from each saved score. Then the test compared the new scores with these changed saved scores. It still required an exact match.

Most saved scores changed. After that, every score matched exactly. This proved that the planned change was the only change.

### Other ways to solve it

- **Save new reference results.** Run the new code and save its output as the new "correct" results. This is fast. But it also accepts your mistakes. Use it only when you review every difference by hand.
- **Review the differences by hand.** Compare old and new results, and read each difference. This works for a few cases, but not for hundreds.
- **Allow a tolerance.** Accept small differences, for example scores within 1 point. This is good for results that change a little by nature, such as model outputs. But it can hide a small real bug.
- **Put the change behind a switch.** A switch, also called a feature flag, turns the new rule on or off. Run the old test with the switch off, and test the new rule on its own. This makes it easy to go back. But you must remove the old code later.

### The lesson

When you change a system on purpose, change the expected results in the same way. Then keep the strict test. It still catches every change that you did not plan.
```

Done when every kept lesson is in exactly one file, and every lesson has its parts in order.

## 6. Check

Reread every sentence that you wrote, and fix each one that breaks a rule:

- ASD-STE100 Simplified Technical English: one idea per sentence, no sentence over 20 words, everyday words, active voice.
- Each term is explained the first time it appears in a file.
- No file, function, ticket, product, company, or person name from the project.
- Each fact in "The situation" and "What we did" matches the transcript.

Done when every sentence in the files you changed passes all four rules.

## 7. Report

In chat, in the same plain language, list each lesson title with its idea in one line. Then list the files you created or changed.
