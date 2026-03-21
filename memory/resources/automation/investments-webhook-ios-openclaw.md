# Investments Automation (iOS + XP + OpenClaw)

_Date: 2026-03-21_
_Status: completed and operational_

## Objective

Build a practical and reliable flow to automatically update Atlas live investment files, reducing friction and dependency on manual chat-based logging.

Specific objective:

1. capture investment events on iPhone;
2. send those events to OpenClaw securely;
3. automatically update the portfolio reference files:
   - `memory/user/investments-portfolio-live.md`
   - `memory/user/investments-proventos-live.md`

## Context and constraints

- Broker: XP.
- Mobile platform: iOS.
- Critical limitation: iOS does not allow fully automatic background capture of third-party app notifications (such as XP) in an unrestricted way.
- Practical conclusion: the best viable model is **shortcut-based quick input + automatic webhook submission**.

## What was implemented

## 1) Live-file standardization

Two core files were consolidated for continuous operation:

- `memory/user/investments-portfolio-live.md`
- `memory/user/investments-proventos-live.md`

Older transitional investment files were removed to keep a clean single source of truth.

## 2) OpenClaw webhook ingestion

Applied OpenClaw configuration:

- hooks enabled;
- dedicated auth token;
- security restrictions (allowed agent, session policy, payload size limit);
- mapped endpoint:
  - `POST /hooks/investments`

This endpoint receives a simple JSON payload (`event/ativo/valor/data/fonte`) and triggers internal processing.

## 3) iPhone → OpenClaw connectivity through Tailnet

Since the gateway was loopback-only, it was changed to tailnet bind and validated on tailnet IP:

- `http://100.106.52.10:18789/hooks/investments`

In the iOS Shortcut, submission uses:

- `Authorization: Bearer <token>`
- `Content-Type: application/json`
- JSON body with event fields.

## 4) Production validation (controlled test)

- Initial error identified: wrong usage of `/hooks/agent` without `message` (`message required`).
- Fix applied: switch to `/hooks/investments` with compatible body.
- Dividend event was received and applied automatically.
- Manual rollback of a fictitious test value was performed and logged correctly.

## Key learnings

1. **Fully passive automation is not realistic on iOS for this case** (XP notifications), but low-friction automation is fully viable.
2. **Correct endpoint + correct payload** is the reliability core.
3. **Standardizing on two live files** reduces complexity and prevents memory drift.
4. **Change logs are mandatory** for auditability.
5. Financial automations must include a clear rollback path for test entries.

## Final result

Final state achieved:

- functional iOS Shortcut → OpenClaw webhook flow;
- automatic updates for live investment files enabled;
- simplified and operational investment memory base;
- auditable process with in-file logs.

## Reusable pattern for future automations

Replicable architecture:

1. lightweight client capture (shortcut/form);
2. secure webhook with token;
3. standardized event parser;
4. deterministic application into operational memory;
5. change log + rollback mechanism.

This pattern can be reused for:

- personal expense capture;
- recurring task flows;
- HR/operations event capture for business routines;
- periodic monitoring with reconciliation.

## Next ideas

1. create separate shortcuts for `provento`, `compra`, `venda` with prefilled payloads;
2. add idempotency via `event_id` to prevent duplicates;
3. add a weekly reconciliation routine (consistency check);
4. include structured webhook response for explicit success/error feedback on iPhone;
5. evolve to deterministic script-based transformation when event volume grows.
