---
description: Fetch a Jira ticket's details (description, acceptance criteria, references), explore the codebase to identify relevant code, and produce a structured implementation plan.
---

# Ticket Plan

## When to use this skill

Use this skill when the user wants to understand a Jira ticket and /jira-ticket <ticket-url>`.

## Input

`$ARGUMENTS` — a Jira ticket URL (e.g., `https://optimizely.atlassian.net/browse/PMOD-1234`) or a plain ticket key (e.g., `PMOD-1234`).

## Prerequisites

This skill depends on the **Atlassian MCP** being configured. The tools it calls (`mcp__atlassian__getJiraIssue`, `mcp__atlassian__getConfluencePage`) only exist when that MCP is installed.

Check if it is set up:

```bash
claude mcp list | grep atlassian
```

If it is missing, install it:

```bash
claude mcp add --transport http atlassian https://mcp.atlassian.com/v1/sse
```

Then restart Claude Code. Re-run `claude mcp list` to confirm it shows up. The first call to a Jira tool will trigger an OAuth flow in the browser.

If the MCP cannot be installed (no permission, offline, the MCP is unreachable), stop and tell the user. Do not try to scrape Jira via `WebFetch` as a fallback. Ticket bodies are private and `WebFetch` will not authenticate.

## Steps

### 1. Extract the ticket key

- If the argument is a URL, extract the ticket key from it (the last path segment, e.g., `PMOD-1234`).
- If the argument is already a key, use it directly.
- Also extract the Jira site hostname from the URL for use as the `cloudId`. If the argument is just a key, ask the user for the Jira site URL.

### 2. Fetch ticket information

Use the `mcp__atlassian__getJiraIssue` tool to fetch the ticket details:
- Summary
- Description
- Acceptance criteria (often in the description or a custom field)
- Any linked issues, epic links, or attachments
- Comments (may contain context or decisions)

Use `responseContentFormat: "markdown"` for readable output.

If the ticket references Confluence pages, fetch those too using `mcp__atlassian__getConfluencePage`.

### 3. Summarize the ticket

Present a clear summary to the user:
- **Ticket**: key + summary
- **Description**: what the ticket asks for
- **Acceptance Criteria**: bullet list
- **References**: any linked tickets, Confluence pages, or external links mentioned

### 4. Explore the codebase

Based on the ticket's requirements:
- Search for relevant files, classes, functions, and patterns in the codebase
- Read key files to understand current behavior
- Identify which parts of the code will need changes
- Note any existing patterns that should be followed

### 5. Create the implementation plan

Present the plan in this exact structure using simple and easy english:

```
## Implementation Plan: [Ticket Key] — [Short Title]

### 1. Why are we doing this?
(What problem are we solving? Connect to user/business value.)

### 2. What are we trying to build/change?
(High-level explanation, no jargon. What will be different after this work?)

### 3. Where in the codebase does this happen?
(Specific files and modules that will be touched, with brief notes on each.)
```

### 6. Review with the user

After presenting the plan, pause and let the user review it. Answer questions, refine sections, and iterate until the user is satisfied.

## Important notes

- Do NOT start implementing anything. This skill is for planning only.
- Always wait for user approval before executing the plan.
- If the ticket references other tickets or pages, fetch and incorporate that context.
- Be specific about file paths — don't say "the service layer", say `src/app/services/evaluation_service.py`.