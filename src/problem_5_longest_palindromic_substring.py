#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#


# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Determines the longest palindrome in the input string.
        """

        if len(s) < 2:
            return s

        odd_start_idx = 0
        odd_end_idx = 0

        # Initialize the palindrome edge tracking indices such that the first
        # two lines of the next loop cause the two central indices to be
        # compared first.
        even_start_idx = 1
        even_end_idx = 0

        odd_center_idx = 0

        # The center index in the even case points to the left index of the
        # two central indices.
        even_center_idx = 0

        # Store the longest palindrome of the sequence in the form [start_idx,
        # end_idx], where square brackets imply inclusivity, not list syntax.
        longest_palindrome = (0, 0)

        # At the start of the loop, the algorithm assumes that the current
        # substring indicated by the start and end indices is a palindrome.
        # This is true in the base case, since: in the odd case, idx 0 -> idx 0
        # (inclusive) is equivalent to s[0] (a single character is a
        # palindrome) and in the even case, idx 1 -> idx 0 (inclusive) is
        # equivalent to an empty string (the largest even-sized palindrome
        # assumable without comparing characters for equality).
        while odd_center_idx < len(s) or even_center_idx + 1 < len(s):
            # ====== ODD CASE ======

            # Update the start and end indices.
            odd_start_idx -= 1
            odd_end_idx += 1

            # Check if the start and end indices extend the palindrome.
            if (
                odd_center_idx < len(s)
                and (odd_start_idx >= 0 and odd_end_idx < len(s))
                and (s[odd_start_idx] == s[odd_end_idx])
            ):
                longest_palindrome = self._get_longer_substring(
                    longest_palindrome, (odd_start_idx, odd_end_idx)
                )

            # If they don't, move the palindrome center forward, and repeat.
            else:
                odd_center_idx += 1
                odd_start_idx = odd_end_idx = odd_center_idx

            # ====== EVEN CASE ======

            # Update the start and end indices.
            even_start_idx -= 1
            even_end_idx += 1

            # Check if the start and end indices extend the palindrome.
            if (
                even_center_idx + 1 < len(s)
                and (even_start_idx >= 0 and even_end_idx < len(s))
                and (s[even_start_idx] == s[even_end_idx])
            ):
                longest_palindrome = self._get_longer_substring(
                    longest_palindrome, (even_start_idx, even_end_idx)
                )

            # If they don't, move the palindrome center forward, and repeat.
            else:
                even_center_idx += 1

                # Initialize the new palindrome edge tracking indices such that the
                # first two lines of the next loop cause the two central indices to
                # be compared first.
                even_start_idx = even_center_idx + 1
                even_end_idx = even_center_idx

        return s[longest_palindrome[0] : longest_palindrome[1] + 1]

    def _get_longer_substring(
        self, a: tuple[int, int], b: tuple[int, int]
    ) -> tuple[int, int]:
        return a if a[1] - a[0] > b[1] - b[0] else b


# @lc code=end
