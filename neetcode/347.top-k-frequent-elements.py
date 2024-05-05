#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create key: count
        hm = defaultdict(lambda: 0)
        for num in nums:
            hm[num] += 1
        return heapq.nlargest(k, iterable=hm.keys(), key=hm.get)

        
# @lc code=end



