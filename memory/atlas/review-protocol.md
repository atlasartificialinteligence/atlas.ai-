# Review Protocol (Atlas)

## Purpose
Define a consistent weekly review workflow for structural maintenance of the Second Brain.

## Cadence
- Weekly (Sunday 18:00 America/Sao_Paulo) via scheduled cron job.

## Standard workflow (ordered)
1. Root Governance Check
2. Memory Taxonomy Integrity Check
3. Quality & Redundancy Scan
4. Weekly Change Log consolidation
5. Continuity Risks & Gaps
6. Next-week Top 3 focus

## Output contract
Every weekly review must publish sections A-G:
- A) Executive summary
- B) Weekly changes (new/modified/merged/archived/deleted)
- C) Structural problems with severity
- D) Top 3 recommended actions
- E) Pending alignments with Erick
- F) Execution transparency (executed/not executed/no-change)
- G) Per-file diff summary (or explicit no-diff statement)

## Decision rules
- Preserve MEMORY.md as curated and compact.
- Keep root files short and high-signal.
- Prefer archive over deletion when uncertain.
- Mark uncertainty explicitly.
- High-risk/destructive changes require explicit alignment.

## Evidence discipline
- Use full paths whenever possible.
- Distinguish clearly:
  - actions performed in the current run
  - historical changes detected from prior periods.
