from uuid import UUID
from interest_account.factory import InterestAccountFactory
from interest_account.api import StatsAPI

user_id = UUID("00000000-0000-0000-0000-000000000001")

api = StatsAPI()
api.set_income(user_id, 2500.00)

factory = InterestAccountFactory(api)
account = factory.create(user_id)

# Simula saldo existente
account.deposit("1000.00")

# Aplica juros
account.apply_interest()

# Exibe extrato
for tx in account.get_statement():
    print(tx)
