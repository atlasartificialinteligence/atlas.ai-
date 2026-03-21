# Dividends by Stock — Live (Atlas)

_Last updated: 2026-03-21 21:02 UTC_
_Status: validated_

## Accumulated dividends by stock (R$)

| Stock | Accumulated Dividends (R$) |
|---|---:|
| BBAS3 | 3,228.21 |
| PETR4 | 2,162.05 |
| BBSE3 | 791.47 |
| EGIE3 | 256.70 |
| SAPR4 | 179.03 |
| ENBR3 | 166.12 |
| AESB3 | 37.08 |

## Grand total

- **R$ 6,820.66**

## Update Automation (active)

This file is the automatic destination for dividend events received via Atlas webhook.

When Atlas receives a valid `ATLAS_EVENT` with `event=provento`:

- add the value to the stock in `Accumulated Dividends (R$)`;
- create the stock row if it does not exist yet;
- recalculate `Grand total`;
- record the update in `Change Log`.

### Event operational format (reference)

`ATLAS_EVENT tipo=<provento|compra|venda> ativo=<TICKER> valor=<VALUE> data=<DD/MM/YYYY> fonte=ios_shortcut`

### Operational policy

- `event=provento` automatically updates this file.
- `event=compra`/`event=venda` do not directly update this file.
- Invalid/incomplete events must be blocked and flagged for review.

## Data sources

> **Inactive for now** — this section will be activated once we define the official file/source structure.

## Change Log

- 2026-03-21 18:12 UTC — created live dividends-by-stock file with consolidated accumulated values.
- 2026-03-21 20:45 UTC — added formal webhook automation guideline (`ATLAS_EVENT`) for automatic dividend updates.
- 2026-03-21 20:54 UTC — `provento` event applied: PETR4 + R$ 40.03 (source: ios_shortcut; informed date: 21/03/2026).
- 2026-03-21 20:57 UTC — manual rollback of fictitious test: PETR4 - R$ 40.03; values restored to original state.
- 2026-03-21 21:02 UTC — `provento` event applied: PETR4 + R$ 31.48 (source: ios_shortcut; informed date: 20/03/2026).
