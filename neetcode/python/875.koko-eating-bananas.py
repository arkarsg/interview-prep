#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def can_finish(piles, mid):
            time_taken = 0

            for num_bananas in piles:
                time_taken += math.ceil(num_bananas / mid)
            return time_taken <= h    

        high = max(piles)
        low = 1

        while low < high:
            mid = low + (high - low) // 2
            if can_finish(piles, mid):
                high = mid
            else:
                low = mid + 1
        return high
# @lc code=end

