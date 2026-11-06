from proration.billing import monthly_charge
from proration.models import Plan


def test_whole_month_charges_the_full_monthly_price() -> None:
    plan = Plan("plan_standard", 3_000)

    assert monthly_charge(plan, 2026, 6) == 3_000


def test_each_plan_charges_its_own_price() -> None:
    standard = Plan("plan_standard", 3_000)
    flexible = Plan("plan_flexible", 3_600)

    assert monthly_charge(standard, 2026, 6) == 3_000
    assert monthly_charge(flexible, 2026, 2) == 3_600
