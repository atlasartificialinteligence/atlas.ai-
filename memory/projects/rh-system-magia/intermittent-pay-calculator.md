# Project Note — Magia RH System (Long-Term)

## Project Status
- Status: Active (long-term, continuous)
- Start date: 2026-03-26
- Owner: Erick (business/process owner)
- System steward: Atlas

## Project Vision
Build an internal RH system for Supermercado Magia to reduce manual work, increase process reliability, and improve operational speed.

This is not a one-off build. It is a continuous system project that will evolve in modules.

## Initial Module (Kickoff)
### Intermittent Employee Salary Calculator
First module to be developed inside the RH system.

### Problem
Intermittent employees are paid by worked hour, and final compensation varies by:
- role/function;
- number of worked days/hours in period;
- role-specific additions (e.g., insalubridade, quebra de caixa, periculosidade).

Recruiters need fast, transparent, and consistent salary projections during interviews.

### Objective of Module v1
Provide a reliable salary simulation tool for intermittent roles that outputs:
- estimated daily pay;
- estimated weekly pay;
- estimated monthly pay;
- clear calculation memory (how values were derived).

## Why This Matters
- Reduces manual calculation time in RH.
- Improves transparency with candidates.
- Improves consistency of interview communication.
- Creates a practical entry point to broader RH process automation.

## Strategic Direction
The RH calculator is the first module of a broader internal RH system.
Future modules may include:
- admission workflow;
- document/checklist pipeline;
- operational dashboards;
- integration layers (later stage, only after process maturity).

## Operating Principles
- Start simple and high-impact.
- Validate in real operation before adding complexity.
- Preserve auditability and formula transparency.
- Keep legal/HR rules explicit and versioned.
- Expand in controlled iterations.

## Maintenance Rule (Mandatory)
This note is a living project artifact.
It must be updated as the project evolves.

Update this note whenever one of the following happens:
- scope change;
- new module approval;
- rule change in compensation logic;
- architecture decision;
- milestone completion;
- major risk discovered;
- strategic pivot.

## Next Step (Current)
Collect and formalize v1 business rules from existing Excel logic:
- function catalog;
- base hourly rate per function;
- additions per function and incidence rules;
- projection scenarios (daily/weekly/monthly).
