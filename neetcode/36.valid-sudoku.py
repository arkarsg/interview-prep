#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkRows(board):
            for i in range(len(board)):
                rowSet = set()
                for j in range(len(board[i])):
                    if board[i][j] in rowSet:
                        return False
                    if board[i][j] != ".":
                        rowSet.add(board[i][j])
            return True

        def checkColumns(board):
            for col in range(0, 9):
                colSet = set()
                for elem in range(0,9):
                    if board[elem][col] in colSet:
                        return False
                    if board[elem][col] != ".":
                        colSet.add(board[elem][col])
            return True

        def checkBoxes(board):
            for i in range(0, 9, 3):
                for j in range(0, 9, 3):
                    nums = set()
                    for k in range(3):
                        for l in range(3):
                            num = board[i+k][j+l]
                            if num in nums:
                                return False
                            if num != ".":
                                nums.add(num)
            return True


        return checkRows(board) and checkColumns(board) and checkBoxes(board)

# @lc code=end

