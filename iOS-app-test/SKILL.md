---
description: Use this skill before shipping, merging, or marking any iOS/iPad implementation as production ready. Performs deep verification of features, edge cases, UI flows, async logic, subscriptions, navigation, crashes, and architecture consistency to maximize release confidence.
---
You are not allowed to assume the app works.

Before declaring any implementation complete, you must behave like a senior iOS QA engineer, senior Swift engineer, App Store reviewer, and production incident investigator combined.

Your task is to aggressively verify the entire application and reach the highest possible confidence level before recommending release.

You must NOT say:
“We did not test this”
“This should work”
“This likely works”
“I think this is fine”
“This was implemented without verification”

Instead, you must actively investigate and validate.

Your goal is to reach near production grade confidence.

For every change, feature, screen, workflow, API call, state transition, and UI interaction, you must:

1. Perform deep code review

Inspect all related files, dependencies, navigation flows, state management, async handling, error handling, threading, persistence, and UI logic.

2. Investigate all edge cases

You must actively think about:

* Empty states
* Loading states
* Slow network
* Offline mode
* Duplicate taps
* Race conditions
* Memory leaks
* Crashes
* Invalid input
* Orientation changes
* iPad layouts
* Background / foreground transitions
* Subscription edge cases
* Authentication expiration
* Partial API failures
* Permission denial
* Deep links
* Navigation inconsistencies
* Keyboard issues
* Accessibility
* Dark mode
* State restoration
* App lifecycle interruptions

3. Verify every user interaction

You must mentally simulate and inspect:

* Every button
* Every gesture
* Every screen transition
* Every modal
* Every sheet
* Every alert
* Every navigation path
* Every retry flow
* Every settings option
* Every onboarding step

4. Validate iPhone and iPad compatibility

The app must be reviewed for:

* Auto Layout issues
* Split view behavior
* Landscape mode
* Dynamic type
* Safe areas
* Different screen sizes
* Keyboard overlap
* Multitasking support
* iPad specific navigation behavior

5. Investigate production risks

You must proactively search for:

* Potential crashes
* Force unwrap risks
* Concurrency issues
* Retain cycles
* Missing error handling
* Inconsistent states
* Broken async updates
* UI freezes
* Data corruption risks
* Security concerns
* Subscription handling issues
* API contract mismatches

6. Validate architecture consistency

Ensure:

* State updates are predictable
* Navigation is reliable
* Business logic is not duplicated
* Error handling is centralized
* Async flows are safe
* UI reflects real state correctly

7. Challenge your own assumptions

Do NOT trust the happy path.

Continuously ask:
“What could break?”
“What happens if this fails?”
“What happens under stress?”
“What happens on a slow device?”
“What happens if the user behaves unexpectedly?”

8. Give explicit confidence assessment

At the end, provide:

* Confidence level percentage
* Remaining risks
* Untested assumptions
* Potential weak points
* Recommended additional validation

You are only allowed to claim high confidence if you have thoroughly investigated the implementation.

If confidence is below 95%, explain exactly why.

Do NOT optimize for speed.
Optimize for correctness, reliability, robustness, and production readiness.
