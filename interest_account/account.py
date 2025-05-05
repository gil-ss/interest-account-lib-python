from decimal import Decimal
from uuid import UUID
from .money import to_money
from .models import Transaction


class InterestAccount:
    """
    Represents a user's interest-bearing account.

    This class is responsible for managing:
        - The account balance
        - Transaction history
        - Accumulated interest below deposit threshold

    It uses Decimal for precise monetary representation and relies on utility
    functions for safe money rounding and conversion.
    """

    def __init__(self, user_id, interest_rate: float) -> None:
        """
        Initializes the account with a user ID and interest rate.

        Args:
            user_id (UUID): The account owner ID.
            interest_rate (float): Interest rate percentage (e.g., 0.5 for 0.5%).
        """
        self.user_id: UUID = user_id
        self.interest_rate: float = interest_rate
        self.balance: Decimal = to_money("0")  # Always stored as Decimal
        self.transactions = []
        self.skipped_interest: Decimal = to_money("0")


    def deposit(self, amount) -> None:
        """
        Deposits a valid monetary amount into the account.

        Args:
            amount (str | int | Decimal): The deposit amount.

        Raises:
            ValueError: If the deposit amount is zero or negative.
        """
        money = Decimal(amount)

        if money <= Decimal("0.00"):
            raise ValueError("Deposit amount must be positive.")

        self.balance += money
        self.transactions.append(Transaction(amount=money, type="DEPOSIT"))
