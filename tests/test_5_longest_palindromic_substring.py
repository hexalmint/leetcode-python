import pytest

from problem_5_longest_palindromic_substring import Solution


@pytest.fixture
def s():
    return Solution()


# Tests for _binary_search
@pytest.mark.parametrize(
    "string, expected",
    [
        ("", ""),
        ("a", "a"),
        ("ac", "a"),
        ("aa", "aa"),
        ("aba", "aba"),
        ("ababba", "abba"),
        ("ababababba", "abababa"),
        ("a" + ("ba" * 50), "a" + ("ba" * 50)),
    ],
)
def test_binary_search(s: Solution, string: str, expected: str):
    assert s.longestPalindrome(string) == expected
