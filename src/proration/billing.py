"""Monthly plan charges.

Customers are billed monthly for their price plan. Today the service supports
whole-month billing only: the invoice charges the plan's full monthly price.
Mid-month plan changes are not supported yet — that is ticket BILL-140.
"""

from __future__ import annotations

from proration.models import Plan


def monthly_charge(plan: Plan, year: int, month: int) -> int:
    """A customer's charge for one month on `plan`, in whole pence.

    Whole-month billing only: the charge is the plan's full monthly price.
    Mid-month plan changes are not supported yet (BILL-140).
    """
    return plan.monthly_price_pence