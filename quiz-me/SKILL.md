---
name: quiz-me
description: Quiz me with back-and-forth questions until I fully understand your last response.
disable-model-invocation: true
argument-hint: "[part to focus on, or pasted text]"
---

The user read a response and wants to understand all of it. Run a **teach-back** session. The user explains each idea in their own words, and you correct them until every idea is right.

The target is the last assistant response before this command. If the user gave an argument, it either names the part to focus on or is pasted text to use as the target. If there is no earlier response and no pasted text, ask the user to paste the text.

## Language

Write every message in ASD-STE100 Simplified Technical English. This covers the idea list, the questions, the feedback, the re-teaching, and the close.


## 1. Build the idea list

Break the target into its key ideas. A key idea is one claim, number, decision, or cause and effect that the response depends on. Put them in order, so each idea comes after the ideas it needs.

Make sure each idea is true before you teach it. If an idea rests on code or data and you are not sure of it, check it. When the response was wrong or unclear, tell the user first, then teach the correct version.

Your first message shows the idea list as short titles, then asks the first question. Keep the explanations back; the user gives those.

Done when every key idea is on the list. Test: a reader who knew only the listed ideas could rebuild the response.

## 2. Confirm each idea

Work through the list in order. Each message has this shape:

- The idea marker, for example "Idea 2 of 5".
- Feedback on the last answer, in one to three lines.
- One question.

Each question asks the user to explain the idea in their own words, apply it to a new case, predict what changes when something changes, or say why the idea matters. A one-word answer cannot satisfy it, and the answer is not a sentence they can copy from the response.

Judge each answer, then act:

- **Right.** Say exactly what was right. Then ask about the same idea from a new angle, a little harder.
- **Partly right.** Name the right part and the missing or wrong part. Give one hint. Ask again from a new angle.
- **Wrong.** Explain the idea again in smaller steps, with a concrete example from the user's current work. Then ask from a new angle, because the same question again only tests whether the user can repeat your words.
- **"I don't know".** Teach the idea in small steps, then ask an easier question about it.
- **The user asks their own question.** Answer it fully, then go back to the current idea.

An idea is confirmed when the user has done both of these correctly, in their own words:

1. Explained what the idea says and why it is true.
2. Applied it to a new case that the response did not mention.

Move to the next idea only when the current idea is confirmed. Write down every wrong belief the user showed; step 3 checks them again. When the user answers right on the first try, make the next questions harder. When they struggle, make the steps smaller.

## 3. Check the whole picture

Ask the user to explain the whole response in a few sentences, as if to a teammate who did not read it. Then ask one question that needs two or more ideas together. Then check each wrong belief from step 2 again with a fresh question.

Done when the summary has every key idea and nothing false, and each earlier wrong belief now gets a right answer. When something fails, go back to that idea in step 2.

## 4. Close

Give a short summary:

- Ideas confirmed on the first try.
- Ideas that needed help, each with its correct version in one line.
- Any correction you made to the original response.
