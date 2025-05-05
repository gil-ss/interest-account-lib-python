from dataclasses import dataclass
from decimal import Decimal
from enum import Enum, auto
from datetime import datetime
from uuid import UUID


class TransactionType(Enum):
    """
    Enumerates all possible types of account transactions.
    This is used to distinguish between deposits and interest accruals.
    """
    DEPOSIT = "deposit"
    INTEREST = "interest"


@dataclass
class Transaction:
    """
    A financial operation that modifies the balance of an interest account.

    Attributes:
        user_id (UUID): The ID of the account owner.
        amount (Decimal): The transaction value (always positive).
        type (TransactionType): The kind of transaction (deposit or interest).
        timestamp (datetime): Date and time of the operation.
    """
    user_id: UUID
    amount: Decimal
    type: TransactionType
    timestamp: datetime
