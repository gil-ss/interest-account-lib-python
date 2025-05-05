from interest_account.money import to_money
import pytest


def test_should_convert_string_to_decimal():
    # We want to be able to convert "10.50" into a money-safe decimal value
    from interest_account.money import to_money

    result = to_money("10.50")

    assert str(result) == "10.50"


def test_to_money_should_raise_type_error_for_float():
    with pytest.raises(TypeError):
        to_money(0.01)
