from decimal import Decimal


def to_money(value: str | int | Decimal) -> Decimal:
    if isinstance(value, float):
        raise TypeError("Avoid using float. Use string, int, or Decimal to represent money.")

    return Decimal(value)