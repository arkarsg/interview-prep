#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_so_far = 0
        left = 0
        right = len(height) - 1

        while left < right:
            actual_height = min(height[left], height[right])
            max_so_far = max(max_so_far, actual_height * (right - left))
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1
                right -= 1
        return max_so_far
# @lc code=end

