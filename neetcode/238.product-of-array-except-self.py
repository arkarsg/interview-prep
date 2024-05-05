#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        curr = 1
        for num in nums:
            res.append(curr)
            curr *= num
        curr = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= curr
            curr *= nums[i]
        return res
# @lc code=end

