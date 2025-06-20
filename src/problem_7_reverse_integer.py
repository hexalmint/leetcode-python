#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start


class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        x = -x if is_negative else x

        y = 0
        while x > 0:
            digit = x % 10

            # Check for potential overflow on this step
            if (
                is_negative
                and (-y < -214_748_364 or (-y == -214_748_364 and digit > 8))
            ) or (
                not is_negative
                and (y > 214_748_364 or (y == 214_748_364 and digit > 7))
            ):
                return 0

            y *= 10
            y += digit

            x //= 10

        return -y if is_negative else y


# @lc code=end
