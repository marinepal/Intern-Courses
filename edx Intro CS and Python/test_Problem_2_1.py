import pytest

import Problem_2_1

valuesList = [(42, 0.2, 0.04, 31.38),
              (484, 0.2, 0.04, 361.61),
              (281, 0.12, 0.04, 194.01),
              (214, 0.12, 0.06, 114.76)
              ]


def setup_module(module):
    print("~~~~~~~~~~~~~~~~~~~~setup~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def teardown_module(module):
    print("~~~~~~~~~~~~~~~~~~~~teardown~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


@pytest.mark.parametrize("balance, monthIR, monthPR, answer", valuesList)
def test_remBal(balance, monthIR, monthPR, answer):
    assert Problem_2_1.remainingBalance(balance, monthIR, monthPR) == answer


@pytest.mark.parametrize("balance, monthIR, monthPR, answer", valuesList)
def test_remBalRec(balance, monthIR, monthPR, answer):
    assert Problem_2_1.remainingBalanceRecursive(balance, monthIR, monthPR) == answer

# testing the new keys
