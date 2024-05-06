#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(list(
            filter(
                lambda char: char.isalnum(),
                s
            )
        )).lower()
        left_ptr = 0
        right_ptr = len(s) - 1
        while left_ptr < right_ptr:
            if s[left_ptr] == s[right_ptr]:
                left_ptr += 1
                right_ptr -= 1
                continue
            else:
                return False
        return True
        
# @lc code=end

