class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def rowValid(row, num):
            for i in range(9):
                if board[row][i] == str(num):
                    return False
            return True
        
        def colValid(col, num):
            for i in range(9):
                if board[i][col] == str(num):
                    return False
            return True
        
        def boxValid(row, col, num):
            boxRow = row - (row % 3)
            boxCol = col - (col % 3)
            for i in range(3):
                for j in range(3):
                    if board[boxRow + i][boxCol + j] == str(num):
                        return False
            return True

        def backtrack(board):
            for row in range(9):
                for col in range(9):
                    if board[row][col] == ".":
                        for num in range(1, 10):
                            if rowValid(row, num) and colValid(col, num) and boxValid(row, col, num):
                                board[row][col] = str(num)
                                if backtrack(board):
                                    return True
                                else:
                                    board[row][col] = "."
                        return False
            return True

        backtrack(board)
                
