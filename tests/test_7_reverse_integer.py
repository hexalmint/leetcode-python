from typing import Optional
import pytest

from problem_7_reverse_integer import Solution


@pytest.fixture
def s():
    return Solution()


@pytest.mark.parametrize(
    "x, expected",
    [
        (0, 0),
        (1, 1),
        (12, 21),
        (123, 321),
        (1230, 321),
        (12300, 321),
        (1_463_847_412, 2_147_483_641),
        (1_463_847_413, 0),
        (-1, -1),
        (-12, -21),
        (-123, -321),
        (-1230, -321),
        (-12300, -321),
        (-1_463_847_412, -2_147_483_641),
        (-1_463_847_413, 0),
        (-1563847412, 0),
    ],
)
def test_add_two_numbers(
    s: Solution,
    x: int,
    expected: int,
):
    assert s.reverse(x) == expected
