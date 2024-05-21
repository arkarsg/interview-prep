#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [a_1, ... , a_n]
        # [ a_k, a_k+1, ... , a_0, ..., a_k-1]
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2
            if nums[low] <= nums[-1]:
                high = mid - 1
            else:
                low = mid + 1

        def binarySearch(nums, left, right, target):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return None

        answer = binarySearch(nums, 0, low - 1, target) or binarySearch(nums, low, len(nums) - 1, target)
        return answer or -1
        
# @lc code=end
nums = [1]
target = 3
print(Solution().search(nums, target))
