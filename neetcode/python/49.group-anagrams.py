#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}

        for word in strs:
            lookup = ''.join(sorted(word))
            if lookup in hm:
                hm[lookup].append(word)
            else:
                hm[lookup] = [word]
        return list(hm.values())
        
# @lc code=end

