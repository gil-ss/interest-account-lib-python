from decimal import Decimal


def to_money(value: str) -> Decimal:
    return Decimal(value)