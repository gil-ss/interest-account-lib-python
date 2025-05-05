from interest_account.api import StatsAPI
from uuid import uuid4
from decimal import Decimal

def test_set_and_get_monthly_income():
    api = StatsAPI()
    user_id = uuid4()
    income = Decimal("2500.00")
    api.set_income(user_id, income)
    assert api.get_monthly_income(user_id) == income


def test_get_interest_rate_based_on_income():
    assert StatsAPI.get_interest_rate(Decimal("900.00")) == 0.5
    assert StatsAPI.get_interest_rate(Decimal("1000.00")) == 0.5
    assert StatsAPI.get_interest_rate(Decimal("1000.01")) == 0.93
    assert StatsAPI.get_interest_rate(Decimal("4000.00")) == 0.93
    assert StatsAPI.get_interest_rate(Decimal("4000.01")) == 1.02
