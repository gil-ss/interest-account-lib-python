from uuid import UUID
from decimal import Decimal


class StatsAPI:
    def __init__(self) -> None:
        self._data = {}

    def set_income(self, user_id: UUID, income: Decimal) -> None:
        self._data[user_id] = income

    def get_monthly_income(self, user_id: UUID) -> Decimal:
        return self._data[user_id]
