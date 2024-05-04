#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        ref_set = defaultdict(lambda: 0)
        for char in s:
            ref_set[char] += 1

        for char in t:
            ref_set[char] -= 1
            if ref_set[char] < 0:
                return False
        return True
        
# @lc code=end

