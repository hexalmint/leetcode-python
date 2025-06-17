from typing import Optional
import pytest

from problem_2_add_two_numbers import Solution, ListNode


@pytest.fixture
def s():
    return Solution()


@pytest.mark.parametrize(
    "l1, l2, expected",
    [
        # 1. 123 + 123 = 246
        (
            ListNode(1, ListNode(2, ListNode(3))),
            ListNode(1, ListNode(2, ListNode(3))),
            ListNode(2, ListNode(4, ListNode(6))),
        ),
        # 2. 0 + 0 = 0
        (ListNode(0), ListNode(0), ListNode(0)),
        # 3. 999 + 1 = 1000
        (
            ListNode(9, ListNode(9, ListNode(9))),
            ListNode(1),
            ListNode(0, ListNode(0, ListNode(0, ListNode(1)))),
        ),
        # 4. 0 + 123 = 123
        (
            ListNode(0),
            ListNode(3, ListNode(2, ListNode(1))),
            ListNode(3, ListNode(2, ListNode(1))),
        ),
        # 5. 123 + 0 = 123
        (
            ListNode(3, ListNode(2, ListNode(1))),
            ListNode(0),
            ListNode(3, ListNode(2, ListNode(1))),
        ),
        # 6. 5 + 5 = 10
        (ListNode(5), ListNode(5), ListNode(0, ListNode(1))),
        # 7. 18 + 0 = 18
        (ListNode(8, ListNode(1)), ListNode(0), ListNode(8, ListNode(1))),
        # 8. 1 + 9999999 = 10000000
        (
            ListNode(1),
            ListNode(
                9,
                ListNode(
                    9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))
                ),
            ),
            ListNode(
                0,
                ListNode(
                    0,
                    ListNode(
                        0,
                        ListNode(0, ListNode(0, ListNode(0, ListNode(0, ListNode(1))))),
                    ),
                ),
            ),
        ),
        # 9. 342 + 465 = 807
        (
            ListNode(2, ListNode(4, ListNode(3))),
            ListNode(5, ListNode(6, ListNode(4))),
            ListNode(7, ListNode(0, ListNode(8))),
        ),
        # 10. 1 + 999 = 1000
        (
            ListNode(1),
            ListNode(9, ListNode(9, ListNode(9))),
            ListNode(0, ListNode(0, ListNode(0, ListNode(1)))),
        ),
        # 11. 9999 + 1 = 10000
        (
            ListNode(9, ListNode(9, ListNode(9, ListNode(9)))),
            ListNode(1),
            ListNode(0, ListNode(0, ListNode(0, ListNode(0, ListNode(1))))),
        ),
        # 12. Unequal length, no carry
        (ListNode(2), ListNode(3, ListNode(4)), ListNode(5, ListNode(4))),
        # 13. Unequal length, with carry
        (ListNode(5), ListNode(5, ListNode(9)), ListNode(0, ListNode(0, ListNode(1)))),
        # 14. 1 + 99999 = 100000
        (
            ListNode(1),
            ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))),
            ListNode(
                0, ListNode(0, ListNode(0, ListNode(0, ListNode(0, ListNode(1)))))
            ),
        ),
        # 15. Two long numbers, multiple carries
        (
            ListNode(9, ListNode(8, ListNode(7, ListNode(6, ListNode(5))))),
            ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4))))),
            ListNode(
                0, ListNode(0, ListNode(0, ListNode(0, ListNode(0, ListNode(1)))))
            ),
        ),
        # 16. Just carry at end
        (ListNode(9, ListNode(9)), ListNode(1), ListNode(0, ListNode(0, ListNode(1)))),
        # 17. Both lists are palindromic
        (
            ListNode(1, ListNode(2, ListNode(1))),
            ListNode(1, ListNode(2, ListNode(1))),
            ListNode(2, ListNode(4, ListNode(2))),
        ),
        # 18. Lists with zeros between
        (
            ListNode(1, ListNode(0, ListNode(1))),
            ListNode(9, ListNode(0, ListNode(9))),
            ListNode(0, ListNode(1, ListNode(0, ListNode(1)))),
        ),
        # 19. Carry propagates entire list
        (
            ListNode(9, ListNode(9, ListNode(9))),
            ListNode(1),
            ListNode(0, ListNode(0, ListNode(0, ListNode(1)))),
        ),
        # 20. Empty l2
        (
            ListNode(1, ListNode(2, ListNode(3))),
            None,
            ListNode(1, ListNode(2, ListNode(3))),
        ),
    ],
)
def test_add_two_numbers(
    s: Solution,
    l1: Optional[ListNode],
    l2: Optional[ListNode],
    expected: Optional[ListNode],
):
    received = s.addTwoNumbers(l1=l1, l2=l2)
    assert received == expected
