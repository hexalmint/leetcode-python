from typing import Optional
import pytest

from problem_20_valid_parentheses import Solution


@pytest.fixture
def s():
    return Solution()


@pytest.mark.parametrize(
    "string, expected",
    [
        ("()", True),
        ("(())", True),
        ("((()))", True),
        (("(" * 50) + (")" * 50), True),
        ("(", False),
        (")", False),
        ("((", False),
        ("(()", False),
        ("(()))", False),
        ("[]", True),
        ("[[]]", True),
        ("[[[]]]", True),
        (("[" * 50) + ("]" * 50), True),
        ("[", False),
        ("]", False),
        ("[[", False),
        ("[[]", False),
        ("[[]]]", False),
        ("{}", True),
        ("{{}}", True),
        ("{{{}}}", True),
        (("{" * 50) + ("}" * 50), True),
        ("{", False),
        ("}", False),
        ("{{", False),
        ("{{}", False),
        ("{{}}}", False),
        ("({[]})", True),
        ("{([])}", True),
        ("[{()}]", True),
        ("([)]", False),
        ("[{(})]", False),
    ],
)
def test_add_two_numbers(
    s: Solution,
    string: str,
    expected: bool,
):
    assert s.isValid(s=string) == expected
