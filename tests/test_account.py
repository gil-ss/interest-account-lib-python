from uuid import uuid4
from interest_account.account import InterestAccount

def test_should_create_account_with_user_id_and_interest_rate():
    user_id = uuid4()
    account = InterestAccount(user_id=user_id, interest_rate=0.5)
    assert account.user_id == user_id
    assert account.interest_rate == 0.5


def test_new_account_should_start_with_zero_balance():
    account = InterestAccount(user_id=uuid4(), interest_rate=0.5)
    assert account.balance == Decimal("0.00")