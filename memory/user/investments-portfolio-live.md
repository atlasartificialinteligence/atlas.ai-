# Investment Portfolio — Live (Atlas)

_Last updated: 2026-03-25 12:53 UTC_
_Status: validated_

## Portfolio Snapshot (current position)

| Stock | Quantity | Current Price (R$) | Avg Cost (R$) | Market Value (R$) | Unrealized P/L (R$) | Unrealized P/L (%) | Portfolio Weight (%) |
|---|---:|---:|---:|---:|---:|---:|---:|
| BBAS3 | 1,479 | 23.27 | 19.934151 | 34,416.33 | 4,933.72 | 16.73% | 81.75% |
| BBSE3 | 53 | 34.09 | 19.03 | 1,806.77 | 798.18 | 79.14% | 4.29% |
| EGIE3 | 35 | 31.31 | 26.396571 | 1,095.85 | 171.97 | 18.61% | 2.60% |
| PETR4 | 69 | 45.67 | 32.838986 | 3,151.23 | 885.34 | 39.07% | 7.49% |
| SAPR4 | 200 | 8.14 | 4.05 | 1,628.00 | 818.00 | 100.99% | 3.87% |

## Portfolio Totals

- Total equity value (R$): **42,098.18**
- Total cost basis (R$): **34,490.97**
- Total unrealized result (R$): **7,607.21**
- Total unrealized result (%): **22.05%**

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
- 2026-03-21 21:38 UTC — manual rollback of fictitious buy test: PETR4 -10 @ R$ 23.51; restored prior quantities, average cost, totals, and weights.
- 2026-03-21 21:38 UTC — event `compra` applied: SAPR4 +100 @ R$ 8.14 (source: ios_shortcut; informed date: 21/03/2026). Recalculated quantity, average cost, totals, and weights.
- 2026-03-21 21:42 UTC — manual rollback of fictitious buy test: SAPR4 -100 @ R$ 8.14; restored prior quantities, average cost, totals, and weights.
- 2026-03-25 12:53 UTC — event `compra` applied: BBAS3 +229 @ R$ 23.98 (source: ios_shortcut; informed date: 23/03/2026). Recalculated quantity, average cost, totals, and weights.
