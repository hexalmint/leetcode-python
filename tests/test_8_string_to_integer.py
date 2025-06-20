import pytest

from problem_8_string_to_integer import Solution


@pytest.fixture
def s():
    return Solution()


@pytest.mark.parametrize(
    "string, expected",
    [
        ("1", 1),
        ("12", 12),
        (" ", 0),
        ("  +1", 1),
        ("-2", -2),
        (" +1234a", 1234),
        ("  -2147483649", -2_147_483_648),
        (" 2147483648abc", 2_147_483_647),
    ],
)
def test_add_two_numbers(
    s: Solution,
    string: str,
    expected: int,
):
    assert s.myAtoi(s=string) == expected
