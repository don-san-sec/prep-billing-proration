# Prorating plan changes

Prorating a Brightwatt Energy customer's monthly charge when they change price
plan mid-month.

## Context

Brightwatt Energy is an app-first UK domestic energy supplier. About 180,000
customers pay a monthly bill, and every amount is stored in whole pence.

Customers can switch price plan at any time from the app, and a switch takes
effect the same day. Plenty of switches land mid-month, so a month with a
switch has a chunk of days on the old plan and a chunk on the new one.

The ticket for this work is BILL-140:

> "Prorate the monthly charge when a customer changes plan mid-month."

## The billing handbook's proration rules

These come from the billing team's handbook. The invoice our systems produce
must match it exactly, or month-end reconciliation against the finance ledger
fails.

1. When a customer changes plan mid-month, the invoice charges the **old plan
   for the days before the change** and the **new plan for the rest of the
   month**.
2. The **change day itself belongs to the new plan**.
3. A plan's daily rate in a month is its **monthly price ÷ the number of days
   in that calendar month**. February is 28 or 29 days; never a flat 30, and
   never 365/12.
4. **Round only the final total**, half up to whole pence. Do not round daily
   rates or intermediate parts.
5. A change effective **on the 1st** means the whole month is on the new plan.

Worked examples from the handbook:

- June (30 days), change effective the 10th: **9 days** on the old plan and
  **21 days** on the new plan.
- February 2026 has 28 days, so a plan at 2800p has a daily rate of **100p**
  that month.
- A change effective on the 1st charges **0 days** on the old plan.

## How it works

```
src/proration/
  models.py           Plan, PlanChange
  billing.py          monthly_charge(); whole-month charges
tests/
```

Proration itself isn't implemented yet. The monthly billing run (not part of
this service) picks the plan to bill; this service owns the plan models and
the charge shown on the bill. Mid-month plan changes are not supported yet.

## Running locally

```
uv sync
uv run pytest -q
```

## Your task

A colleague has opened a PR: https://github.com/don-san-sec/prep-billing-proration/pull/1. You are the owner of this feature. Review the PR and decide whether to accept or reject it, and explain why.
