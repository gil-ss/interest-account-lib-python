from decimal import Decimal
from uuid import UUID
from .money import to_money
from .models import Transaction, TransactionType
from datetime import datetime, timezone
from .money import round_money


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
        self.transactions.append(Transaction(
            user_id=self.user_id,
            amount=money,
            type=TransactionType.DEPOSIT,
            timestamp=datetime.now(timezone.utc)
        ))


    def apply_interest(self) -> None:
        """
        Applies interest to the account based on the current balance and interest rate.

        - Interest is only added if the computed amount is >= 0.01.
        - If it's less than 0.01, it is stored in `skipped_interest` until it accumulates enough.

        This ensures that small interest amounts are not lost due to rounding.
        """
        # Calculate raw interest
        raw_interest = (self.balance * Decimal(self.interest_rate)) / Decimal("100")

        # Add any previously skipped interest
        total_interest = raw_interest + self.skipped_interest
        total_interest = round_money(total_interest)

        if total_interest >= Decimal("0.01"):
            self.balance += total_interest
            self.transactions.append(Transaction(
                user_id=self.user_id,
                amount=total_interest,
                timestamp=datetime.now(timezone.utc),
                type=TransactionType.INTEREST
            ))
            self.skipped_interest = to_money("0")
        else:
            self.skipped_interest += raw_interest


    def get_statement(self) -> list[dict]:
        """
        Returns a chronological list of all account transactions.

        Each transaction is represented as a dictionary with:
            - amount
            - type
            - timestamp (ISO 8601 format)

        Returns:
            List[Dict]: All transactions in the order they occurred.
        """
        return [
            {
                "amount": str(tx.amount), # string for compatibility
                "type": tx.type.name,
                "timestamp": tx.timestamp.isoformat()
            }
            for tx in self.transactions
        ]
