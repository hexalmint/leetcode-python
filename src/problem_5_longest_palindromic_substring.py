#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#


# TODO: This algorithm fails to check for existing palindromes within the
# current palindrome when palindrome tracking stops. For instance, consider
# the example "abababa". The algorthm will recognize "aba" and "abababa",
# but not "ababa".
# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Calculates the longest palindrome in a given string.

        The algorithm operates on the input string with three index pointers.
        The first is a current index pointer, always pointing to the last seen
        letter in the string. The second pointer is a pointer for palindromes
        of even length. This pointer starts one index less than the current
        index pointer. The third pointer is a pointer for palindromes of odd
        length. This pointer starts two indices less than the current index
        pointer.

        Even Palindrome Tracking:
        For each character seen, that character is compared with the character
        at the index of the even pointer. If the two characters are the same,
        the even pointer is decremented, leading to the previous character
        being compared in the next iteration. Otherwise, tracking on the
        current palindrome stops. Then, the longest palindrome is updated per
        the "Longest Palindrome Updates" section.

        Odd Palindrome Tracking:
        For each character seen, that character is compared with the character
        at the index of the odd pointer. If the two characters are the same,
        the odd pointer is decremented, leading to the previous character being
        compared in the next iteration. Otherwise, tracking on the current
        palindrome stops. Then, the longest palindrome is updated per the
        "Longest Palindrome Updates" section.

        Note that per iteration, the even-length palindrome is always shorter
        than the odd-length palindrome (before palindrome tracking stops for
        the first time). Thus, odd-length palindromes are tracked after even-
        length palindromes in a given iteration.

        Boundaries Reached:
        There are two instances where even and odd palindrome tracking is
        overruled. That's when the even/odd pointer reaches the start of the
        input string or the current index pointer reaches the end of the input
        string. In both cases, palindrome tracking is stopped by force. Then,
        the longest palindrome is updated per the "Longest Palindrome Updates"
        section.

        Longest Palindrome Updates:
        To update the longest palindrome, the length of the current palindrome
        being tracked is compared to the longest known palindrome. If the
        length of the current palindrome is larger, the longest palindrome is
        replaced with the current palindrome.
        """

        if len(s) < 2:
            return s

        longest_palindrome = s[0]
        even_ptr = 0
        odd_ptr = 0
        for idx in range(1, len(s)):
            # If the left edge of the string was reached, determine the
            # palindrome length and update stats.
            if even_ptr == -1:
                palindrome_len = idx - even_ptr - 1
                if palindrome_len > len(longest_palindrome):
                    longest_palindrome = s[even_ptr + 1 : idx]

                # Set the even pointer.
                even_ptr = idx - 1 if s[idx] == s[idx - 1] else idx

            # If the right edge of the string is reached, determine the
            # palindrome length and update stats.
            elif idx == len(s) - 1:
                if s[idx] == s[even_ptr]:
                    palindrome_len = idx - even_ptr + 1
                    if palindrome_len > len(longest_palindrome):
                        longest_palindrome = s[even_ptr:]

                else:
                    palindrome_len = idx - even_ptr - 1
                    if palindrome_len > len(longest_palindrome):
                        longest_palindrome = s[even_ptr + 1 : -1]

            # If the palindrome continues, decrement the even pointer.
            elif s[idx] == s[even_ptr]:
                even_ptr -= 1

            # If the palindrome stops here, determine the palindrome length
            # and update stats.
            else:
                palindrome_len = idx - even_ptr - 1
                if palindrome_len > len(longest_palindrome):
                    longest_palindrome = s[even_ptr + 1 : idx]

                # Set the even pointer.
                even_ptr = idx - 1 if s[idx] == s[idx - 1] else idx

            if idx < 2:
                continue

            # If the left edge of the string was reached, determine the
            # palindrome length and update stats.
            if odd_ptr == -1:
                palindrome_len = idx - odd_ptr - 1
                if palindrome_len > len(longest_palindrome):
                    longest_palindrome = s[odd_ptr + 1 : idx]

                # Set the odd pointer.
                odd_ptr = idx - 1 if s[idx] == s[idx - 1] else idx - 1

            # If the right edge of the string is reached, determine the
            # palindrome length and update stats.
            elif idx == len(s) - 1:
                if s[idx] == s[odd_ptr]:
                    palindrome_len = idx - odd_ptr + 1
                    if palindrome_len > len(longest_palindrome):
                        longest_palindrome = s[odd_ptr:]

                else:
                    palindrome_len = idx - odd_ptr - 1
                    if palindrome_len > len(longest_palindrome):
                        longest_palindrome = s[odd_ptr + 1 : -1]

            # If the palindrome continues, decrement the odd pointer.
            elif s[idx] == s[odd_ptr]:
                odd_ptr -= 1

            # If the palindrome stops here, determine the palindrome length
            # and update stats.
            else:
                palindrome_len = idx - odd_ptr - 1
                if palindrome_len > len(longest_palindrome):
                    longest_palindrome = s[odd_ptr + 1 : idx]

                # Set the odd pointer.
                odd_ptr = idx - 1 if s[idx] == s[idx - 1] else idx - 1

        return longest_palindrome


# @lc code=end
