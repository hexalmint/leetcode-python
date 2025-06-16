import pytest

from problem_5_longest_palindromic_substring import Solution


@pytest.fixture
def s():
    return Solution()


# Tests for _binary_search
@pytest.mark.parametrize(
    "test_string, expected",
    [("aba", "aba"), ("ababababba", "abababa"), ("a" + ("ba" * 50), "a" + ("ba" * 50))],
)
def test_binary_search(s, test_string, expected):
    assert s.longestPalindrome(test_string) == expected
