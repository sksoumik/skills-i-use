This is a collection of Claude Code & Codex skills I’ve been using recently. It’s an evolving repo that I plan to continuously improve and expand.

>Most of these skills are based on publicly available work from other creators on GitHub. I’ve modified some to suit my workflow, and built a few entirely from scratch.

Use the command for your agent, or mention the skill name in your request.

| Skill | What it does | When to use it | Claude Code | Codex |
|---|---|---|---|---|
| `ask-me` | Runs an interactive codebase mentoring session with one question at a time. | Use it to improve your understanding of a codebase, its design, and its tradeoffs. | `/ask-me` | `$ask-me` |
| `code-review` | Reviews changes against repository standards and the source specification. | Use it to review a branch, pull request, or work since a known Git point. | `/code-review` | `$code-review` |
| `diagnosing-bugs` | Finds the root cause of bugs and performance regressions. | Use it when code fails, throws an error, gives a wrong result, or becomes slow. | `/diagnosing-bugs` | `$diagnosing-bugs` |
| `distill` | Extracts lessons that you can reuse in other projects and companies. | Use it after a work session that produced useful technical or process lessons. | `/distill` | `$distill` |
| `domain-modeling` | Defines project terms, domain concepts, and architecture decisions. | Use it to create or update a glossary or architecture decision record. | `/domain-modeling` | `$domain-modeling` |
| `explain` | Rewrites the previous response as a clear, visual, beginner-friendly explanation. | Use it when you need to understand findings, decisions, blockers, or next actions. | `/explain` | `$explain` |
| `find-skills` | Finds agent skills that can add a requested capability. | Use it when you want to know whether an installable skill exists for a task. | `/find-skills` | `$find-skills` |
| `grill-me` | Uses a strict interview to find gaps in a plan or design. | Use it before you accept a plan, design, or important technical decision. | `/grill-me` | `$grill-me` |
| `grill-with-docs` | Reviews a plan through questions and records decisions in project documents. | Use it when you also need architecture decision records or glossary updates. | `/grill-with-docs` | `$grill-with-docs` |
| `grilling` | Tests an idea, plan, or decision with difficult questions. | Use it when you want to test assumptions and expose weak reasoning. | `/grilling` | `$grilling` |
| `handoff` | Converts the current conversation into a compact handoff document. | Use it when another agent or person must continue the work. | `/handoff` | `$handoff` |
| `iOS-app-design` | Redesigns and checks iPhone and iPad interfaces for product and engineering quality. | Use it for an iOS or iPadOS redesign, or before you approve the interface for release. | `/iOS-app-design` | `$iOS-app-design` |
| `iOS-app-test` | Checks iOS features, flows, state, subscriptions, crashes, and architecture. | Use it before you ship, merge, or mark an iOS implementation as ready. | `/iOS-app-test` | `$iOS-app-test` |
| `impeccable` | Designs, audits, and improves web and native user interfaces. | Use it for UI design, UX review, accessibility, motion, responsive behavior, or design-system work. | `/impeccable` | `$impeccable` |
| `implement` | Implements work from a specification or ticket set. | Use it after the requirements and work items are clear. | `/implement` | `$implement` |
| `implement-spec` | Implements the output from `to-spec` and `to-tickets`. | Use it when those planning skills have produced an approved specification and tickets. | `/implement-spec` | `$implement-spec` |
| `improve-codebase-architecture` | Finds module design problems and creates a visual report of improvement options. | Use it when you want to find and discuss architecture improvements in an existing codebase. | `/improve-codebase-architecture` | `$improve-codebase-architecture` |
| `jira-ticket` | Reads a Jira ticket, finds the related code, and prepares an implementation plan. | Use it before you start work from a Jira ticket. | `/jira-ticket` | `$jira-ticket` |
| `pr-review` | Reviews a pull request against the main branch and prepares concise review comments. | Use it when you need a detailed pull request review without posting comments. | `/pr-review` | `$pr-review` |
| `quiz-me` | Tests your understanding of the previous response through questions. | Use it when you want active practice instead of another explanation. | `/quiz-me` | `$quiz-me` |
| `re-verify` | Checks each important claim against code or an authoritative source. | Use it when you need proof, file references, or a correction of the previous response. | `/re-verify` | `$re-verify` |
| `retro` | Reviews a coding session and extracts lessons and follow-up actions. | Use it after a session, feature, incident, or difficult implementation. | `/retro` | `$retro` |
| `rubric-gate` | Defines a task-specific quality rubric, grades the work, and fixes weak areas. | Use it when every quality dimension must meet a high score before completion. | `/rubric-gate` | `$rubric-gate` |
| `tdd` | Implements features and fixes with a red, green, refactor test cycle. | Use it when you want tests to define the behavior before implementation. | `/tdd` | `$tdd` |
| `teach` | Teaches a skill or concept within the current workspace. | Use it when you want guided learning with examples from the active project. | `/teach` | `$teach` |
| `tldr` | Reduces the previous response to a short summary and key points. | Use it when the previous response is correct but too long. | `/tldr` | `$tldr` |
| `to-questionnaire` | Converts an unresolved decision into questions for another person. | Use it when the work needs information or approval that you cannot provide. | `/to-questionnaire` | `$to-questionnaire` |
| `to-spec` | Converts the current conversation into a specification and publishes it to the issue tracker. | Use it when the discussion already contains enough detail and does not need another interview. | `/to-spec` | `$to-spec` |
| `to-tickets` | Splits a plan or specification into small linked delivery tickets. | Use it when you need ordered work items with clear dependencies. | `/to-tickets` | `$to-tickets` |
| `triage` | Classifies issues and external pull requests and prepares agent-ready briefs. | Use it when new work must move through a consistent triage process. | `/triage` | `$triage` |
| `understand` | Studies a complete codebase without changing it. | Use it before implementation when you need a verified model of the system, data flow, tests, and infrastructure. | `/understand` | `$understand` |
| `unslop` | Removes common AI writing patterns while it preserves the meaning. | Use it to make documentation and prose direct, plain, and natural. | `/unslop` | `$unslop` |
| `wait-what` | Explains the previous message again with a different approach. | Use it when the previous explanation did not make sense. | `/wait-what` | `$wait-what` |
| `wayfinder` | Maps work that is too large for one agent session into decision tickets. | Use it for a long project with unresolved decisions and several dependent work streams. | `/wayfinder` | `$wayfinder` |
| `website-design` | Redesigns and checks websites for UI, UX, accessibility, responsive behavior, and production quality. | Use it for a full website redesign or before you approve a web interface for release. | `/website-design` | `$website-design` |
| `wizard` | Creates an interactive Bash guide for steps that a person must perform. | Use it for credentials, infrastructure consoles, migrations, or other human-only operations. | `/wizard` | `$wizard` |
| `writing-for-agents` | Writes instructions and documents that agents can follow. | Use it when you create or edit skills, `AGENTS.md`, or `CLAUDE.md`. | `/writing-for-agents` | `$writing-for-agents` |
