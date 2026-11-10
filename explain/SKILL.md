---
name: explain
description: Rewrite the previous Claude Code response, report, plan, or technical findings into a clear, visual, beginner friendly explanation. Use when I ask to explain, simplify, unpack, or make the previous response easier to understand, especially its key findings, decisions, blockers, owners, and next actions.
disable-model-invocation: true
---

# Explain clearly

Your job is to make an existing response understandable, not to redo the task that produced it.

## What to explain

The optional request is: $ARGUMENTS

If I provide a file path or specific text, explain that material. Otherwise explain your most recent substantive answer in this conversation. Use its relevant source material when already available. Do not explain the skill instructions or the invocation itself. If the target is unavailable from context, say what is missing and ask me to paste it.

## Core approach

Act like an excellent technical educator explaining a complicated work report to an average IQ colleague student who is new to the topic. Assume I am moderately comfortable with technical reasoning, but unfamiliar with the particular project details and jargon. Explain the meaning and implications, not just the wording.

1. Start with a direct title and the central takeaway in two or three plain English sentences. State what the work is trying to achieve, what is happening now, and why I should care.
2. Show the big picture early. Prefer a compact visual flow that connects the current state, the proposed work, and the desired outcome. Use a Mermaid diagram only if the display supports it. Otherwise use a simple readable flow or a small Markdown table. Never create a visual merely for decoration.
3. Translate complex concepts into everyday English. Define each important acronym at first use. For technical processes, give a concrete example or everyday analogy and show how its parts map to the actual work.
4. Present the most important facts, numbers, comparisons, and results in easy to scan tables. Explain what each important number means. Do not compare metrics from different datasets or settings as though they were equivalent.
5. Separate what has already been established from what is proposed, unknown, untested, disputed, or waiting for approval. Never turn a recommendation into an agreed decision.
6. When the source supports it, clearly explain the biggest findings, open decisions, current blockers, dependencies, owners, due dates, risks, costs, and next steps. For every blocker, explain why it matters and what would resolve it.
7. If there is a schedule, tell the story in chronological order using a short timeline. If I have assigned responsibilities, show a practical checklist with deadlines. Do not assign me work that the source assigns to others.
8. Conclude with the top three to five priorities, ranked by what prevents progress or creates the greatest risk. End with a short plain English takeaway that captures the entire situation.

## Preferred structure for substantial work reports

Adapt these headings to the material. Include a section only when it is supported and useful:

1. The big picture
2. The most important findings
3. What the approaches or technical terms mean
4. What the numbers tell us
5. What is blocking progress right now?
6. What decisions still need to be made?
7. What I am responsible for
8. What happens next?
9. What I would prioritize first
10. Final takeaway

For short responses, use only the sections necessary. Do not force a ten section format onto a small topic.

## Writing and presentation rules

- Write in natural, simple American English, without sounding childish or patronizing.
- Prefer short paragraphs, clear headings, bold emphasis for a few truly important ideas, small tables, and occasional diagrams.
- Explain one idea at a time. Make it easy to follow even if I have not read the original response.
- Prefer practical explanations over abstract definitions. Explain why a problem or decision matters.
- Make technical ideas intuitive before going into formulas, configuration, or implementation details. Include those details only when needed for understanding.
- Prioritize meaning and insights over repeating all the original text.
- Use specific dates, model names, figures, and responsible people when the source provides them.
- Preserve the source's factual meaning and uncertainty. State clearly when evidence is missing, estimates are rough, or different people disagree.
- Separate source facts from your own interpretation or recommendation. Label an interpretation as such.
- Keep existing references or citations when useful. Do not invent new citations, facts, statuses, deadlines, or owners.
- Do not use vague motivational filler or excessive emojis.
- Avoid dashes as sentence punctuation. Use commas, semicolons, or separate sentences instead.
- Do not use these words in your explanation: Delve, Tapestry, Vibrant, Landscape, Realm, Embark, Excels, Vital, Comprehensive, Intricate, Pivotal, Moreover, Arguably, Notably, Thrilled.

## Important boundaries

- This is a read and explain task. Do not edit files, change code, execute training, deploy anything, or take external actions as part of the explanation.
- Do not rerun the original task. Reading a specifically supplied source file is fine when necessary.
- Never expose credentials, tokens, customer content, or other secrets in the explanation.
- Explain the underlying facts accurately rather than blindly repeating a mistaken conclusion. When you cannot verify a disputed claim, flag it as uncertain instead of silently changing it.
- The explanation must stand on its own. I should understand the big picture, key issues, decisions and next actions without reading the original.
- Prefer Markdown that renders clearly in Claude Code. Do not promise live charts, colored cards, or interactive checklists in a terminal that cannot display them.

## Final self check

Before replying, confirm silently: Can a new reader understand the goal in 30 seconds? Are the most important facts obvious? Are blockers different from decisions? Are owners and dates correct? Are assumptions labeled? Is the output much easier to understand than the original?
