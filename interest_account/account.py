from decimal import Decimal

class InterestAccount:
    def __init__(self, user_id, interest_rate):
        self.user_id = user_id
        self.interest_rate = interest_rate
        self.balance = Decimal("0.00")
        self.transactions = []
