from datetime import date

from proration.models import Plan, PlanChange
from proration.proration import prorated_month_charge


def test_mid_month_change_in_june() -> None:
    old_plan = Plan("plan_standard", 3_000)
    new_plan = Plan("plan_flexible", 3_600)
    change = PlanChange("cus_0001", old_plan, new_plan, date(2026, 6, 10))

    assert prorated_month_charge(old_plan, new_plan, change, 2026, 6) == 3_400


def test_month_without_a_change_is_billed_in_full() -> None:
    plan = Plan("plan_standard", 3_000)

    assert prorated_month_charge(plan, plan, None, 2026, 6) == 3_000