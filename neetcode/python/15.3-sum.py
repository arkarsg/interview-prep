#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        positives = []
        negatives = []
        zeroes = []
        
        for num in nums:
            if num > 0:
                positives.append(num)
            elif num < 0:
                negatives.append(num)
            else:
                zeroes.append(num)

        p_lookup, n_lookup = set(positives), set(negatives)

        if zeroes:
            if len(zeroes) >= 3:
                res.add((0, 0, 0))

            for num in p_lookup:
                neg_num = -1 * num
                if neg_num in n_lookup:
                    res.add((neg_num, 0, num))

        for i in range(len(negatives)):
            for j in range(i+1, len(negatives)):
                pos_num = -1 * (negatives[i] + negatives[j])
                if pos_num in p_lookup:
                    res.add(tuple(sorted((negatives[i], negatives[j], pos_num))))
    
        for i in range(len(positives)):
            for j in range(i+1, len(positives)):
                neg_num = -1 * (positives[i] + positives[j])
                if neg_num in n_lookup:
                    res.add(tuple(sorted((neg_num, positives[i], positives[j]))))
        return res
                            
# @lc code=end

