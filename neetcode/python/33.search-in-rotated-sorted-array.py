class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [a_1, ... , a_n]
        # [ a_k, a_k+1, ... , a_0, ..., a_k-1]
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            elif nums[low] <= nums[mid]:
                if target > nums[mid] or target < nums[low]:
                    low = mid + 1
                else:
                    high = mid -1
            else:
                if target < nums[mid] or target > nums[high]:
                    high = mid - 1
                else:
                    low = mid + 1
        return -1


