import pytest

from case.pytest_allure.func.calculator import Calculator

@pytest.fixture(scope="session")
def calculator():
    return Calculator()
