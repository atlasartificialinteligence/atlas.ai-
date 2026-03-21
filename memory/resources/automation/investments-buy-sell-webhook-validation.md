# Buy/Sell Automation Validation (iOS + OpenClaw)

_Date: 2026-03-21_
_Status: validated with controlled tests and rollback_

## Objective

Validate and harden the webhook-based automation for buy/sell events so that portfolio updates are applied consistently and can be safely reversed after fictitious tests.

## Scope

Automation path validated:

- iOS Shortcut (`Atlas - Compra`) sends JSON payload to `POST /hooks/investments`.
- OpenClaw receives and processes event payload for `event=compra` / `event=venda`.
- Atlas updates `memory/user/investments-portfolio-live.md`.

## Payload standard used

```json
{
  "event": "compra",
  "ativo": "<TICKER>",
  "qtd": <NUMBER>,
  "preco": <NUMBER>,
  "data": "DD/MM/YYYY",
  "fonte": "ios_shortcut"
}
```

## What was learned

1. Endpoint/payload mismatch is the main failure source.
   - Using `/hooks/agent` with event-only payload causes `message required`.
   - Correct path for event payload is `/hooks/investments`.
2. Validation must differ by event type.
   - `provento`: requires `ativo`, `valor`, `data`.
   - `compra` / `venda`: requires `ativo`, `qtd`, `preco`, `data`.
3. Verification must account for asynchronous execution.
   - Checking files before hook completion can create false negatives.
   - Reliable check requires file `Last updated` + `Change Log` + completed run status.
4. Rollback is mandatory for controlled fictitious tests.

## Result

- Buy test was successfully applied via webhook automation.
- Quantity/average-cost/totals/weights were updated in `investments-portfolio-live.md`.
- Controlled rollback was executed to restore baseline values.
- Process is now operational for real buy/sell events with safer verification logic.

## Operational guardrails

- Always use controlled test values before first real event after config changes.
- Log each applied event and each rollback in `Change Log`.
- Keep source of truth limited to live files to avoid drift.
- Treat webhook execution as asynchronous and confirm final state before asserting success/failure.

## Next improvement ideas

1. Add idempotency key (`event_id`) to prevent duplicate processing.
2. Add explicit webhook response schema with validation status.
3. Add deterministic processor script for stricter numeric consistency and less model variance.
4. Add optional periodic reconciliation routine against broker export.
