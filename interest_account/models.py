from dataclasses import dataclass
from decimal import Decimal
from enum import Enum, auto


class TransactionType(Enum):
    """
    Enumerates all possible types of account transactions.
    This is used to distinguish between deposits and interest accruals.
    """
    DEPOSIT = "deposit"
    INTEREST = "interest"


@dataclass
class Transaction:
    amount: Decimal
    type: TransactionType
