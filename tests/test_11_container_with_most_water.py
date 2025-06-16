from typing import List

import pytest

from problem_11_container_with_most_water import Solution

s = Solution()


@pytest.mark.parametrize(
    "height, expected",
    [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([4, 3, 2, 1, 4], 16),
        ([1, 2, 1], 2),
        ([2, 3, 4, 5, 18, 17, 6], 17),
        ([1, 2, 4, 3], 4),
        ([0, 0, 0, 0], 0),
        ([1, 3, 2, 5, 25, 24, 5], 24),
        ([2, 2, 2, 2, 2, 2], 10),
        ([1, 2, 3, 4, 5], 6),
        ([5, 4, 3, 2, 1], 6),
        ([1, 1, 1, 1, 100], 4),
        ([100, 1, 1, 1, 1], 4),
        ([1, 2, 100, 2, 1], 4),
        ([1, 100, 1, 1, 1], 4),
        ([1], 0),
        ([1000, 1000], 1000),
        ([1, 2, 1, 2, 1, 2, 1, 2, 1], 8),
        ([1] * 100, 99),
        ([i for i in range(100)], 2450),
    ],
)
def test_max_area(height: List[int], expected: int):
    assert s.maxArea(height) == expected
