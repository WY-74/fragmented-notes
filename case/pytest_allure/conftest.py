import pytest
from typing import List

from case.pytest_allure.func.calculator import Calculator


@pytest.fixture(scope="session")
def calculator():
    return Calculator()


def pytest_collection_modifyitems(session: "Session", config: "Config", items: List["Item"]) -> None:
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
