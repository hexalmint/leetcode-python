import pytest

from problem_4_median_of_two_sorted_arrays import Solution


@pytest.fixture
def s():
    return Solution()


# Tests for _binary_search
@pytest.mark.parametrize(
    "arr, target, expected",
    [
        ([1, 2], 0, -1),
        ([1, 2], 1, 0),
        ([1, 3], 2, 0.5),
        ([1, 2], 2, 1),
        ([1, 2], 3, 2),
    ],
)
def test_binary_search(s, arr, target, expected):
    assert s._binary_search(arr, target) == expected


# Tests for _combined_index
@pytest.mark.parametrize(
    "arr1, arr2, target, expected",
    [
        ([1], [2], 0, -1),
        ([1], [2], 1, 0),
        ([1], [3], 2, 1),
        ([1], [2], 2, 1),
        ([1], [2], 3, 2),
    ],
)
def test_combined_index(s, arr1, arr2, target, expected):
    assert s._combined_index(arr1, arr2, target) == expected


# Tests for findMedianSortedArrays
@pytest.mark.parametrize(
    "nums1, nums2, expected",
    [
        ([1, 3], [2], 2),
        ([1], [2], 1.5),
        ([1, 2], [3, 4], 2.5),
        ([], [], None),
        ([], [1], 1.0),
        ([], [1, 2], 1.5),
        ([1], [2], 1.5),
        ([1, 2, 3, 4, 5, 6], [100], 4),
        ([1, 2, 3], [10, 11, 12], 6.5),
        ([1, 3, 5], [2, 4, 6], 3.5),
        ([5, 5, 5], [5, 5, 5], 5.0),
        ([-5, -3, -1], [1, 3, 5], 0.0),
        ([1, 4, 7], [2, 3, 6, 8], 4.0),
        ([1], [2, 3, 4, 5, 6, 7, 8, 9], 5.0),
        ([1, 2, 2, 2], [2, 2, 3, 4], 2.0),
        ([1, 2, 2, 2], [2, 2, 3], 2.0),
        ([2, 2, 4, 4], [2, 2, 4, 4], 3.0),
        ([1, 2, 3, 4, 5], [100], 3.5),
        ([1, 2, 3, 4], [5, 6, 7, 8], 4.5),
        ([1, 2, 2, 2, 3], [2, 2, 2, 4, 5], 2.0),
        ([-3, -2, -1], [1, 2, 3, 4], 1.0),
        ([1], [100], 50.5),
        ([1, 1, 1, 1, 1], [1000, 1001, 1002], 1.0),
        ([1, 3, 5, 7, 9, 11], [2, 4, 6, 8, 10, 12], 6.5),
    ],
)
def test_find_median_sorted_arrays(s, nums1, nums2, expected):
    assert s.findMedianSortedArrays(nums1, nums2) == expected
