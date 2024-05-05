#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {val:i for i, val in enumerate(nums)}
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in lookup.keys() and lookup[remainder] != i:
                return [i, lookup[remainder]]
        
# @lc code=end

