#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next

    def __eq__(self, other: Optional["ListNode"]) -> bool:
        if other is None:
            return False

        node = self
        while True:
            if node is None and other is None:
                return True
            elif (node is None and other is not None) or (
                node is not None and other is None
            ):
                return False
            elif node is not None and other is not None:
                if node.val != other.val:
                    return False

                node = node.next
                other = other.next

    def __str__(self) -> str:
        node = self
        values = []
        while node is not None:
            values.append(str(node.val))
            node = node.next

        return " -> ".join(values)


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return None

        head = ListNode()
        node = head

        while l1 is not None or l2 is not None:
            node.val += (l1.val if l1 is not None else 0) + (
                l2.val if l2 is not None else 0
            )

            if node.val >= 10:
                node.val -= 10
                carry = 1

            else:
                carry = 0

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

            if l1 is not None or l2 is not None or carry != 0:
                node.next = ListNode(val=carry)
                node = node.next

        return head


# @lc code=end
