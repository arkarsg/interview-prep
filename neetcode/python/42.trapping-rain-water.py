#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height) - 1
        left = 0
        right = n
        left_max = height[left]
        right_max = height[right]
        res = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(height[left], left_max)
                res += (left_max - height[left]) * 1
            else:
                right -= 1
                right_max = max(height[right], right_max)
                res += (right_max - height[right]) * 1

        return res
# @lc code=end

