from decimal import Decimal, ROUND_HALF_UP


def to_money(value: str | int | Decimal) -> Decimal:
    """
    Converts a raw numeric input into a Decimal formatted as money (2 decimal places).

    Args:
        value (str | float | int | Decimal): Input value to convert.

    Returns:
        Decimal: Normalized monetary value with two decimal places.
    """
    if isinstance(value, float):
        raise TypeError("Avoid using float. Use string, int, or Decimal to represent money.")

    return round_money(Decimal(value))


def round_money(value: Decimal) -> Decimal:
    """
    Rounds a Decimal to two decimal places using standard financial rounding.

    Args:
        value (Decimal): The value to round.

    Returns:
        Decimal: Rounded value.
    """
    return value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
