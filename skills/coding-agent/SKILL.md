---
name: coding-agent
description: Delegate coding tasks to Codex, Claude Code, or Pi agents via background sub-agent sessions. Use when building new features/apps, refactoring code, writing tests, fixing bugs, or running longer coding work that should execute asynchronously.
---

# Coding Agent

Delegate implementation work to a background coding sub-agent, then report results clearly.

## Quick workflow

1. Clarify scope, stack, constraints, and acceptance criteria.
2. Spawn a sub-agent with a concrete coding task.
3. Let it run asynchronously (avoid tight polling loops).
4. Review output, validate key claims, and summarize what changed.
5. Propose next steps (tests, follow-ups, cleanup).

## Task template for delegation

Use this structure in `sessions_spawn` task text:

- Goal
- Repository/workdir
- Required changes
- Tests to run
- Constraints (style, safety, no destructive ops)
- Expected output format (files changed, commands run, summary)

## Quality bar

- Prefer small, verifiable increments.
- Require explicit file paths and diffs in result summaries.
- Ask for test output or reproduction steps when relevant.
- If requirements are ambiguous, ask before delegating.
