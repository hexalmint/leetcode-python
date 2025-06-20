#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#


# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        stack = []

        for _s in s:
            if _s in parentheses:
                if len(stack) == 0 or parentheses[_s] != stack.pop():
                    return False
                else:
                    continue

            stack.append(_s)

        return len(stack) == 0


# @lc code=end
