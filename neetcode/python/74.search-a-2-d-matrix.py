#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#
# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        low = 0
        high = n * m - 1
        while low <= high:
            mid = (high + low) // 2
            num = matrix[mid // m][mid % m]
            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1
        return False
# @lc code=end


