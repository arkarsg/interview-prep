#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        openers = n
        closers = n
        res = []

        def dfs(openers, closers, validParenthesis):
            if openers == 0 and closers == 0:
                res.append(validParenthesis)
                return 
            if openers > 0:
                dfs(openers - 1, closers, validParenthesis + '(')

            if closers > openers:
                dfs(openers, closers-1, validParenthesis + ')')

        dfs(openers, closers, '')
        return res
        
# @lc code=end

