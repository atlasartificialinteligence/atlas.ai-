# Investment Portfolio — Live (Atlas)

_Last updated: 2026-03-21 21:34 UTC_
_Status: validated_

## Portfolio Snapshot (current position)

| Stock | Quantity | Current Price (R$) | Avg Cost (R$) | Market Value (R$) | Unrealized P/L (R$) | Unrealized P/L (%) | Portfolio Weight (%) |
|---|---:|---:|---:|---:|---:|---:|---:|
| BBAS3 | 1,250 | 23.27 | 19.192952 | 29,087.50 | 5,096.31 | 21.24% | 78.14% |
| BBSE3 | 53 | 34.09 | 19.03 | 1,806.77 | 798.18 | 79.14% | 4.85% |
| EGIE3 | 35 | 31.31 | 26.396571 | 1,095.85 | 171.97 | 18.61% | 2.94% |
| PETR4 | 79 | 45.67 | 31.658102 | 3,607.93 | 1,106.94 | 44.26% | 9.69% |
| SAPR4 | 200 | 8.14 | 4.05 | 1,628.00 | 818.00 | 100.99% | 4.37% |

## Portfolio Totals

- Total equity value (R$): **37,226.05**
- Total cost basis (R$): **29,234.65**
- Total unrealized result (R$): **7,991.40**
- Total unrealized result (%): **27.34%**

## Update Automation (active)

This file is integrated with Atlas investment-event webhooks.

When Atlas receives a valid `ATLAS_EVENT`:

- `event=compra` or `event=venda` → automatically update this file (`portfolio live`), recalculating position, average cost, value, and totals.
- `event=provento` → does not change position/average cost, but records the event for reconciliation with the dividends file.

### Event operational format (reference)

`ATLAS_EVENT tipo=<provento|compra|venda> ativo=<TICKER> valor=<VALUE> data=<DD/MM/YYYY> fonte=ios_shortcut`

### Operational policy

- Automatic updates are the default rule for webhook events.
- If any field is inconsistent (invalid ticker, missing value, invalid date), the event must be flagged for manual review.
- Every automatic update must generate a record in `Change Log`.

## Data sources

> **Inactive for now** — this section will be activated once we define the official file/source structure.

## Change Log

- 2026-03-21 18:12 UTC — initial fill with consolidated position, average cost, and per-stock P/L.
- 2026-03-21 20:45 UTC — added formal webhook automation guideline (`ATLAS_EVENT`) for automatic portfolio-live updates.
- 2026-03-21 21:34 UTC — event `compra` applied: PETR4 +10 @ R$ 23.51 (source: ios_shortcut; informed date: 21/03/2026). Recalculated quantity, average cost, totals, and weights.
