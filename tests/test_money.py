import pytest

from interest_account.money import to_money, round_money
from decimal import Decimal


def test_should_convert_string_to_decimal():
    # We want to be able to convert "10.50" into a money-safe decimal value
    from interest_account.money import to_money
    result = to_money("10.50")
    assert str(result) == "10.50"


def test_to_money_should_raise_type_error_for_float():
    with pytest.raises(TypeError):
        to_money(0.01)


def test_to_money_should_accept_int_and_decimal():
    assert to_money(10) == Decimal("10.00")
    assert to_money(Decimal("5.25")) == Decimal("5.25")


def test_round_money_should_round_to_two_decimal_places():
    assert round_money(Decimal("10.555")) == Decimal("10.56")
    assert round_money(Decimal("10.554")) == Decimal("10.55")
    assert round_money(Decimal("10.000")) == Decimal("10.00")
