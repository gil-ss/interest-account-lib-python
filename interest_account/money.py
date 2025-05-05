from decimal import Decimal, ROUND_HALF_UP


def to_money(value: str | int | Decimal) -> Decimal:
    if isinstance(value, float):
        raise TypeError("Avoid using float. Use string, int, or Decimal to represent money.")

    decimal_value = Decimal(value)
    return decimal_value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)