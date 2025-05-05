from uuid import UUID
from .account import InterestAccount
from .api import StatsAPI


class InterestAccountFactory:
    """
    Factory responsible for creating InterestAccount instances.
    It queries the StatsAPI to determine the user's income and maps
    it to the correct interest rate tier before initializing the account.
    """

    def __init__(self, api: StatsAPI) -> None:
        self.api = api


    def create(self, user_id: UUID) -> InterestAccount:
        """
        Creates a new InterestAccount using the user's income retrieved from StatsAPI.

        Args:
            user_id (UUID): The user for whom to create the account.

        Returns:
            InterestAccount: Initialized with the correct interest rate.
        """
        income = self.api.get_monthly_income(user_id)
        interest_rate = self.api.get_interest_rate(income)
        return InterestAccount(user_id=user_id, interest_rate=interest_rate)
