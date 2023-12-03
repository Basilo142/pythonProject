import time

import pytest


@pytest.fixture
def innermost(order):
    order.append("innermost top")


def test_order(order, top):
    time.sleep(3)
    assert order == ["innermost top", "top"]
