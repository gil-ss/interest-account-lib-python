# 💰 Interest Account

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Learning%20Project-yellow)

[![Python Tests](https://github.com/gil-ss/interest-account-lib-python/actions/workflows/python-tests.yml/badge.svg)](https://github.com/gil-ss/interest-account-lib-python/actions/workflows/python-tests.yml)
[![codecov](https://codecov.io/gh/gil-ss/interest-account-lib-python/branch/main/graph/badge.svg)](https://codecov.io/gh/gil-ss/interest-account-lib-python)

A minimal Python library that simulates an interest-bearing savings account.  
It calculates interest based on user income using business rules, tracks deposits, and provides transaction history.

---

### Features

- Deposit money (validated and tracked).
- Skipped interest handling for micro-amounts (< £0.01).
- Income-based interest rates (via Stats API).
- Full transaction history.
- Designed with SOLID principles and unit-tested.

---

### Running Tests

```bash
pytest --cov=interest_account --cov-report=term-missing
```
---

### Project Structure

```
interest_account-lib-python/
├── account.py        # Business logic
├── money.py          # Decimal-safe money utils
tests/
├── test_account.py
├── test_money.py

```

---

### Design Principles

- Clean Architecture (separation of concerns)
- Pythonic idioms (dataclasses, enums, decimal)
- Test-driven development (TDD)
- No database or web framework — **_Pure Logic_** 🧠

---