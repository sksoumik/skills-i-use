---
description: Re-verify every load bearing claim in the last assistant response by quoting the exact file:line in the codebase or citing an authoritative external source. Produces an evidence table plus a rewritten response that contains only verified facts. Use when the user invokes /ds-common:verify-response, says "are you sure", "did you actually check", "verify that", "prove it", "show me where", or "where in the code does it say that".
---

# Verify Response

## When to use this skill

Use this skill when the user wants the **last assistant response** fact checked against the codebase or external sources. The user invokes `/ds-common:verify-response`, or says things like:

- "are you sure"
- "did you actually check"
- "verify that"
- "prove it"
- "show me where in the code"
- "where does it say that"
- "is that real"

This skill exists because LLMs sometimes state things confidently without checking. Function names get pluralized that should not be, line numbers drift after edits, library APIs are misremembered, version numbers come from training data rather than the installed version, and behavior gets described as it "should" work rather than how it actually works. This skill catches all of that for the last response.

It does not audit the whole conversation. Only the last assistant message.

## Rules

### Strict constraints

- NEVER trust the prior response. Treat every claim in it as suspect until verified.
- NEVER mark a claim VERIFIED based on memory, training data, or "I know this". The only valid evidence is a direct quote from a file in the current repo (with `path:line`) or a direct quote from an authoritative external source (with URL).
- NEVER paraphrase the evidence. Quote the literal line so the user can see the exact match.
- NEVER re-use a `path:line` from the prior response as proof. The whole point is to re-check it. Open the file fresh and quote what is actually there now.
- NEVER skip a claim because it "looks obvious". If it was stated as fact, verify it.
- ALWAYS classify hedging language ("should", "probably", "I believe", "I think", "typically") as UNVERIFIED unless real evidence is found.
- ALWAYS state when a claim cannot be verified. Do not silently drop it from the rewritten response.
- ONLY verify load bearing, falsifiable claims. Do not pad the report with opinions, filler, or transitions.

## What counts as a verifiable claim

A claim is verifiable if it is concrete and falsifiable. Examples:

| Verifiable | Not verifiable |
|---|---|
| "`compute_score` is defined in `src/scoring.py`" | "this should work" |
| "the function returns a `dict`" | "this code is clean" |
| "pandas 2.1 deprecated `append`" | "pandas is widely used" |
| "this loop is O(n^2)" | "this is fast enough" |
| "the config has a key `timeout_ms`" | "we probably want a timeout" |
| "Vertex AI `predict` accepts `instances`" | "Vertex AI is good for batch" |
| "we use Python 3.11" | "Python is a good fit here" |
| "there is no rate limiting in `src/api/`" | "rate limiting is a good idea" |

Claims fall into three buckets:

1. **Code references in the current repo**: file paths, function and class names, signatures, type annotations, control flow, "this function does X", "this config has key Y", "there is no X in the codebase".
2. **External facts**: library version behavior, third party API signatures, documentation claims, paper citations, "X is the default in version Y".
3. **Quantitative claims**: complexity ("O(n log n)"), benchmark numbers, "this is faster than", "this uses less memory".

Negative claims ("there is no X") count too. Verify them with a wide grep.

## How to verify

### 1. Read the prior response

Read the most recent assistant message in this conversation. That is the only thing this skill verifies. Ignore earlier turns unless they are needed to interpret what the last message was claiming.

If the prior message had no factual content (just acknowledgment, a clarifying question, a plan), tell the user there is nothing to verify and stop.

### 2. Extract the claims

Walk through the prior response sentence by sentence. For each sentence, decide:

- Is it a falsifiable claim? (use the table above)
- Which bucket: code reference, external fact, or quantitative?

Skip opinions, filler, plans, and questions. Number the claims so the user can refer to them.

Common claim shapes to watch for:

- "The function `X` in `path/to/file.py` does Y."
- "There is no `X` in the codebase."
- "We use library `X` version `Y`."
- "This is the default in `X`."
- "This is O(N)."
- "The bug is at `path:line`."
- "Calling `X` will raise `Y`."
- "The config field `X` controls Y."

### 3. Verify each claim

The verdict for each claim is one of:

- **VERIFIED**: direct evidence found, quoted, with `path:line` or URL.
- **PARTIAL**: claim is partially true but materially misleading. Explain what is right and what is wrong.
- **INCORRECT**: evidence found that contradicts the claim. Show the contradicting evidence.
- **UNVERIFIED**: no evidence found in the repo or from an authoritative source within reasonable effort. Say what was searched so the user can extend the search if they care.

#### Verifying code references

Use Grep, Glob, and Read:

- Run `grep -rn "<symbol>" <suspected path or repo root>` to locate the symbol.
- Read the file at the cited line range to confirm the line says what was claimed.
- Quote the literal line in the evidence column.
- If the claim names a `path:line`, open that exact line. Do not trust the number, re-check it.
- If the claim describes behavior ("this function returns a dict"), read the function body and the return statement. Do not infer from the name.
- For absence claims ("there is no X"), run a wide grep across the repo with relevant synonyms. If grep finds nothing, the absence is VERIFIED.

#### Verifying external facts

Use WebFetch, WebSearch, or the Context7 MCP server:

- **For library API claims, prefer Context7** (`mcp__context7__query-docs`) over web search. It pulls the actual current docs for the specific library version.
- For version specific behavior, fetch the official docs or changelog for that version.
- For academic claims, cite the paper itself (arxiv URL), not a blog summary.

For version claims, **also check the version actually installed in the repo** (`pyproject.toml`, `requirements*.txt`, `package.json`, `go.mod`, `Pipfile.lock`, `poetry.lock`). The installed version is the source of truth here, not the latest version on PyPI.

Quote the source. Include the URL.

#### Verifying quantitative claims

- Complexity claims (O(n), O(log n)): walk through the code and justify, or mark UNVERIFIED.
- Benchmark claims ("X is faster than Y"): require an actual benchmark in the repo or a cited source. Mark UNVERIFIED otherwise.
- "Uses less memory", "scales better": same, require a source.

### 4. Build the evidence table

Format:

```
| # | Claim (paraphrased) | Verdict | Evidence |
|---|---|---|---|
| 1 | `compute_score` lives in `src/scoring.py` | VERIFIED | src/scoring.py:42 — `def compute_score(items: list[Item]) -> float:` |
| 2 | The function returns a `dict` | INCORRECT | src/scoring.py:42 — return type is `float`, not `dict` |
| 3 | pandas 2.1 deprecated `append` | VERIFIED | https://pandas.pydata.org/docs/whatsnew/v2.1.0.html — quoted: "DataFrame.append() ... removed in 2.0" |
| 4 | This is O(n log n) | UNVERIFIED | Code uses a nested loop and a sort. Complexity argument requires more analysis than is available here. |
| 5 | We use Vertex AI SDK v1.40 | INCORRECT | pyproject.toml:23 pins `google-cloud-aiplatform = "^1.52.0"` |
```

Include the table even if every claim is VERIFIED, so the user can see what was checked.

### 5. Rewrite the response

After the table, produce a corrected version of the prior response that:

- Keeps every VERIFIED claim, with the supporting `path:line` or URL inline as proof.
- Drops or corrects every INCORRECT and PARTIAL claim, and is **explicit about the correction**. Do not silently rewrite. The user must see that something changed and why.
- Marks every UNVERIFIED claim with `[UNVERIFIED]` inline, or removes it if the response still reads well without it.
- Does NOT introduce new claims beyond what the prior response contained, unless they are required to correct an error.

Format:

```
## Corrected response

<rewritten content, with [path:line] inline citations for code claims and URL citations for external claims>

### Corrections made
- Claim 2: was "returns a dict", actually returns `float`. Source: src/scoring.py:42.
- Claim 5: was "v1.40", actually `^1.52.0`. Source: pyproject.toml:23.

### Things I could not verify
- Claim 4: the O(n log n) complexity claim. Walk through manually if it matters.
```

If everything was VERIFIED, the rewrite is the original response with inline citations added. Still produce the table; the user wants to see proof, not just trust the verdict.

### 6. Be honest about cost

If verifying a claim requires reading large files, searching the whole repo, or fetching many external docs, do that work. The point of this skill is correctness, not speed. But if a claim is genuinely impossible to verify within reasonable effort (proprietary internal system, dead link, requires running the code), say so under "Things I could not verify" rather than guessing.

## Examples

### Example 1: code reference verification

**Prior response said**: "The `RetryConfig` class in `src/clients/spanner.py` has a default `max_attempts` of 3."

**Verification**:

```bash
grep -n "class RetryConfig" src/clients/spanner.py
```

Read the file at the match. Finds:

```python
class RetryConfig:
    max_attempts: int = 5
```

**Verdict**: INCORRECT. Default is 5, not 3.

**Evidence**: src/clients/spanner.py:17 — `max_attempts: int = 5`.

### Example 2: external fact verification

**Prior response said**: "Pydantic v2 removed the `parse_obj` method."

**Verification**: Use Context7 to query Pydantic docs, or WebFetch the v2 migration guide.

Finds: `parse_obj` is deprecated, not removed. It still works but raises a deprecation warning. Replacement is `model_validate`.

**Verdict**: PARTIAL. The replacement (`model_validate`) is correct, but `parse_obj` was deprecated, not removed.

### Example 3: absence claim

**Prior response said**: "There is no rate limiting in the API layer."

**Verification**:

```bash
grep -rn -iE "rate.?limit|throttle|too_many_requests|429" src/api/
```

If no matches: VERIFIED, the absence is real, with evidence "grep across src/api/ returned 0 hits for rate limiting patterns".

If matches: INCORRECT, quote the matches.

### Example 4: version claim

**Prior response said**: "We are on numpy 1.26 so this API is available."

**Verification**: Read `pyproject.toml` or the lock file. Finds `numpy = "^2.0.0"`.

**Verdict**: INCORRECT. The repo is on numpy 2.x, not 1.26. Then re-check whether the API claim still holds against numpy 2.x using Context7.

## Anti patterns (never do)

- "This looks right based on what I remember" is not verification. Either find the line or mark UNVERIFIED.
- Verifying only the easy claims and skipping the ones that need real digging.
- Paraphrasing the evidence ("the file does say it returns a dict-like object"). Quote the literal line.
- Silently rewriting an incorrect claim in the corrected response without flagging the correction. The user needs to see what changed.
- Re-using the prior response's `path:line` references as proof. Open the file fresh and re-check the line number.
- Marking a claim VERIFIED because it is in your training data. Training data is not evidence.
- Padding the table with non claims ("the assistant was being helpful"). Not falsifiable, skip it.
- Stopping early because "most claims are correct". Verify them all, or be explicit about which were skipped and why.
- Auditing the whole conversation when the user only asked about the last response.
- Producing only the table and no rewritten response. The user asked for both.