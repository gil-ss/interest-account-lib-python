import pytest

from uuid import uuid4
from interest_account.account import InterestAccount
from decimal import Decimal
from interest_account.models import TransactionType


def test_should_create_account_with_user_id_and_interest_rate():
    user_id = uuid4()
    account = InterestAccount(user_id=user_id, interest_rate=0.5)
    assert account.user_id == user_id
    assert account.interest_rate == 0.5


def test_new_account_should_start_with_zero_balance():
    account = InterestAccount(user_id=uuid4(), interest_rate=0.5)
    assert account.balance == Decimal("0.00")


def test_new_account_should_start_with_empty_transaction_list():
    account = InterestAccount(user_id=uuid4(), interest_rate=0.5)
    assert isinstance(account.transactions, list)
    assert len(account.transactions) == 0


def test_new_account_should_start_with_zero_skipped_interest():
    account = InterestAccount(user_id=uuid4(), interest_rate=0.5)
    assert account.skipped_interest == Decimal("0.00")


def test_deposit_should_increase_balance_and_log_transaction():
    account = InterestAccount(user_id=uuid4(), interest_rate=0.5)
    account.deposit("100.50")
    assert account.balance == Decimal("100.50")
    assert len(account.transactions) == 1


def test_deposit_should_raise_error_for_zero_or_negative_amount():
    account = InterestAccount(user_id=uuid4(), interest_rate=0.5)

    with pytest.raises(ValueError, match="must be positive"):
        account.deposit("0.00")

    with pytest.raises(ValueError, match="must be positive"):
        account.deposit("-10")


def test_deposit_should_register_transaction_with_correct_data():
    account = InterestAccount(user_id=uuid4(), interest_rate=0.5)
    account.deposit("100.00")
    tx = account.transactions[0]
    assert tx.amount == Decimal("100.00")
    assert tx.type == TransactionType.DEPOSIT


def test_deposit_should_register_transaction_with_enum_type():
    account = InterestAccount(user_id=uuid4(), interest_rate=0.5)
    account.deposit("100.00")
    tx = account.transactions[0]
    assert tx.amount == Decimal("100.00")
    assert tx.type == TransactionType.DEPOSIT
