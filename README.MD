# 💰 Interest Account 🐍

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Learning%20Project-yellow)

[![Python Tests](https://github.com/gil-ss/interest-account-lib-python/actions/workflows/python-tests.yml/badge.svg)](https://github.com/gil-ss/interest-account-lib-python/actions/workflows/python-tests.yml)
[![codecov](https://codecov.io/gh/gil-ss/interest-account-lib-python/branch/main/graph/badge.svg)](https://codecov.io/gh/gil-ss/interest-account-lib-python)

A minimal Python library that simulates an interest-bearing savings account.  
It calculates interest based on user income using business rules, tracks deposits, and provides transaction history.

---

### Features

- 💵 Safe deposit handling with validation.
- 🧮 Interest applied based on income tiers.
- ⏳ Micro interest (< £0.01) is safely accumulated.
- 🧾 Full transaction log with timestamps.
- 🧰 Built using SOLID, TDD, and Pythonic idioms.
- 📈 100% unit test coverage with `pytest-cov`.

---

### Installation

```bash
git clone git@github.com:gil-ss/interest-account-lib-python.git
cd interest-account-lib-python
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
---

### Usage

``` python
from uuid import uuid4
from interest_account.api import StatsAPI
from interest_account.factory import InterestAccountFactory

user_id = uuid4()

# Setup Stats API
api = StatsAPI()
api.set_income(user_id, 2500.00)

# Create interest-bearing account
factory = InterestAccountFactory(api)
account = factory.create(user_id)

# Interact with the account
account.deposit("100.00")
account.apply_interest()

# Get statement
print(account.get_statement())
```

---

### Running Tests

```bash
pytest --cov=interest_account --cov-report=term-missing
```
###### Ensure 100% coverage:
 - account.py
 - money.py
 - api.py
 - factory.py

---

### Project Structure

```
interest_account-lib-python/
├── account.py        # Business logic
├── api.py            # External API simulation
├── factory.py        # Account creation logic
├── models.py         # Data models
├── money.py          # Decimal-safe money utils
tests/
├── test_account.py
├── test_api.py
├── test_factory.py
├── test_money.py

```

---

---

### CI/CD

This project uses [GitHub Actions](https://github.com/features/actions) for continuous integration and coverage reporting.

- ✅ Automatic test runs on every push and PR
- 📈 Coverage reports via [Codecov](https://codecov.io/)

---

### Design Principles

- 🧼 Clean Architecture (separation of responsibilities).
- 🧪 Test-Driven Development (TDD-first).
- 🐍 Pythonic: dataclasses, enums, Decimal, typing.
- 🧠 Lightweight, no frameworks — just pure logic

---