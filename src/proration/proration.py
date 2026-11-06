"""Prorated monthly charges across a mid-month plan change (BILL-140).

When a customer changes plan mid-month, the invoice charges both plans for
their share of the month, per the billing handbook's proration rules.
"""

from __future__ import annotations

from proration.models import Plan, PlanChange

DAYS_PER_MONTH = 30


def _round_half_up(numerator: int, denominator: int) -> int:
    """Round numerator/denominator half up to a whole number."""
    return (2 * numerator + denominator) // (2 * denominator)


def prorated_month_charge(
    base_plan: Plan,
    new_plan: Plan,
    change: PlanChange | None,
    year: int,
    month: int,
) -> int:
    """The customer's charge for `month`, in whole pence.

    With no plan change, the month is billed on `base_plan` in full. With a
    change, the days before the change are charged on the old plan and the
    rest of the month on the new one.
    """
    if change is None:
        return base_plan.monthly_price_pence

    if (change.effective_date.year, change.effective_date.month) != (year, month):
        raise ValueError(
            f"plan change effective {change.effective_date.isoformat()} "
            f"is outside the billed month {year}-{month:02d}"
        )

    old_plan_days = change.effective_date.day
    new_plan_days = DAYS_PER_MONTH - old_plan_days

    old_plan_total = base_plan.monthly_price_pence * old_plan_days
    new_plan_total = new_plan.monthly_price_pence * new_plan_days

    return _round_half_up(old_plan_total, DAYS_PER_MONTH) + _round_half_up(
        new_plan_total, DAYS_PER_MONTH
    )