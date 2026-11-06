"""Plan and plan-change models."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date


@dataclass
class Plan:
    """A price plan. `monthly_price_pence` is the whole-month price, in pence."""

    plan_id: str
    monthly_price_pence: int


@dataclass
class PlanChange:
    """A customer's move from one plan to another, effective `effective_date`."""

    customer_id: str
    from_plan: Plan
    to_plan: Plan
    effective_date: date