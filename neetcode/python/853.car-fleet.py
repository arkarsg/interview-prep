#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#

# @lc code=start
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed = [
            (position[i], speed[i])
            for i in range(len(speed))    
        ]

        position_speed = sorted(
            position_speed,
            key=lambda pair: pair[0],
            reverse=True
        )

        stack = []
        for pos, speed in position_speed:
            time_taken = (target - pos) / speed
            stack.append(time_taken)

            n = len(stack)
            if n > 1 and stack[n-1] <= stack[n-2]:
                stack.pop()
        return len(stack)
        
# @lc code=end

