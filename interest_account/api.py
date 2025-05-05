from uuid import UUID
from decimal import Decimal


class StatsAPI:
    """
    Simulates an external API that provides user financial statistics.
    Specifically, it retrieves the user's monthly income and maps it to
    a fixed interest rate tier.
    """

    def __init__(self) -> None:
        self._data = {} # Internal mapping: user_id -> monthlyIncome


    def set_income(self, user_id: UUID, income: Decimal) -> None:
        """
        Manually sets the monthly income for a user (used in tests or mocks).

        Args:
            user_id (UUID): The user's unique identifier.
            income (Decimal): The monthly income to store.
        """
        self._data[user_id] = income


    def get_monthly_income(self, user_id: UUID) -> Decimal:
        """
        Simulates GET /users/{userId} -> { "monthlyIncome": ... }

        Args:
            user_id (UUID): The user to retrieve.

        Returns:
            Decimal: The monthly income for that user.

        Raises:
            KeyError: If no income data is found for the user.
        """
        return self._data[user_id]


    @staticmethod
    def get_interest_rate(income: Decimal) -> float:
        """
        Returns the interest rate applicable based on the user's monthly income.

        Business rules:
            - Income ≤ £1,000.00      → 0.50%
            - £1,000.01 to £4,000.00 → 0.93%
            - Income > £4,000.00     → 1.02%

        This method encapsulates the interest-tier logic defined by the business.

        Args:
            income (Decimal): The user's monthly income.

        Returns:
            float: The fixed interest rate (as a percentage) corresponding to the income tier.
        """
        if income <= Decimal("1000.00"):
            return 0.5
        elif income <= Decimal("4000.00"):
            return 0.93
        else:
            return 1.02
