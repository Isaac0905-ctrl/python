import os

import pytest

if os.path.exists('solution.py'):
    from solution import InfiniteList
else:
    from main import InfiniteList  # type:ignore


# ==============================================================================
# FIXTURES
# ==============================================================================


INFLIST1_VALUES = (10, 20, 30, 40, 50)
INFLIST2_VALUES = ('A', 'B', 'C')


@pytest.fixture
def inflist1():
    return InfiniteList(*INFLIST1_VALUES)


@pytest.fixture
def inflist2():
    return InfiniteList(*INFLIST2_VALUES, fill_value='@')
