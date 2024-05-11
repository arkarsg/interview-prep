#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        paren_pairs = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }

        stack = []
        for paren in s:
            if paren in paren_pairs:
                stack.append(paren)
            elif len(stack) == 0 or paren != paren_pairs[stack.pop()]:
                return False
        return len(stack) == 0 
        
# @lc code=end

