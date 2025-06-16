#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
from typing import List


# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        The theory behind this solution operates on the facet that a "good"
        area would be the size of the container from the leftmost container
        wall to the rightmost container wall. Then, the only way to increase
        the size of the container is for the smaller wall to grow, since
        shrinking the larger wall can only decrease the area. Once the left
        and right wall meet, all container sizes larger than the initial
        container size will have been explored.
        """
        left_wall, right_wall = 0, len(height) - 1
        max_area = -1

        # Iterate until the left and right wall touch
        while left_wall < right_wall:
            # Get the current area of the container
            area = min(height[left_wall], height[right_wall]) * (right_wall - left_wall)
            # Update the max area if necessary
            if area > max_area:
                max_area = area

            # Of the two walls, the larger one should be kept, since it is
            # the only one that can potentially increase the container size

            # If the left wall is taller, choose the next right wall
            if height[left_wall] > height[right_wall]:
                right_wall -= 1

            # Otherwise, choose the next left wall
            else:
                left_wall += 1

        return max_area


# @lc code=end
