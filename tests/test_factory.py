from uuid import uuid4
from decimal import Decimal
from interest_account.api import StatsAPI
from interest_account.factory import InterestAccountFactory


def test_factory_should_create_account_with_correct_interest_rate():
    user_id = uuid4()
    income = Decimal("3500.00")  # Should map to 0.93%

    api = StatsAPI()
    api.set_income(user_id, income)

    factory = InterestAccountFactory(api)
    account = factory.create(user_id)

    assert account.user_id == user_id
    assert account.interest_rate == 0.93
    assert account.balance == Decimal("0.00")
    assert account.transactions == []
