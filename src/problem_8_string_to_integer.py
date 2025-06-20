#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start


class Solution:
    def myAtoi(self, s: str) -> int:
        idx = 0

        # Discard the leading white space
        while idx < len(s) and s[idx] == " ":
            idx += 1

        if idx == len(s):
            return 0

        # Check for a positive or negative sign
        is_negative = False
        if s[idx] == "+":
            is_negative = False
            idx += 1

        elif s[idx] == "-":
            is_negative = True
            idx += 1

        # Discard any leading 0s in the number
        while idx < len(s) and s[idx] == "0":
            idx += 1

        # Parse digits from the string
        number = 0
        stoi_map = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
        }
        while idx < len(s) and s[idx] in stoi_map:
            digit = stoi_map[s[idx]]

            # If adding the next digit leads to an overflow, return the rounded number
            if (
                is_negative
                and (number > 214_748_364 or (number == 214_748_364 and digit > 8))
            ) or (
                not is_negative
                and (number > 214_748_364 or (number == 214_748_364 and digit > 7))
            ):
                return -2_147_483_648 if is_negative else 2_147_483_647

            number *= 10
            number += digit
            idx += 1

        return -number if is_negative else number


# @lc code=end
