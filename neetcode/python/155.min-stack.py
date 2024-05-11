#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    def __init__(self):
        self.stack = []
        self.aux = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.aux or val <= self.aux[len(self.aux) - 1]:
            self.aux.append(val)

    def pop(self) -> None:
        popped = self.stack.pop()
        if popped == self.aux[len(self.aux) - 1]:
            self.aux.pop()

    def top(self) -> int:
        n = len(self.stack)
        return self.stack[n - 1]        

    def getMin(self) -> int:
        return self.aux[len(self.aux) - 1]        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

