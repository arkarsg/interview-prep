#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        next_smaller = [n] * n
        prev_smaller = [-1] * n

        stack = []
        for i in range(n):
            # find the index of next smaller element
            while stack and heights[stack[-1]] > heights[i]:
                prev_greater = stack.pop()
                next_smaller[prev_greater] = i
            # find the index of previous smaller element
            if stack:
                prev_smaller[i] = stack[-1]
            stack.append(i)

        area = 0
        for i in range(n):
            curr = heights[i]
            width = next_smaller[i] - prev_smaller[i] - 1
            area = max(area, curr * width)
        return area
        
# @lc code=end

