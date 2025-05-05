from interest_account.api import StatsAPI
from uuid import uuid4
from decimal import Decimal

def test_set_and_get_monthly_income():
    api = StatsAPI()
    user_id = uuid4()
    income = Decimal("2500.00")

    api.set_income(user_id, income)

    assert api.get_monthly_income(user_id) == income
