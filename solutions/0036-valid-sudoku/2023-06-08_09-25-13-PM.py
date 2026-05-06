class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9): #checks the rows
            nums_dict = dict()
            for counter in range(9):
                if board[i][counter] != ".":
                    if board[i][counter] in nums_dict:
                        return False
                    else:
                        nums_dict[board[i][counter]] = 1
        for i in range(9): #checks the columns
            nums_dict = dict()
            for counter in range(9):
                if board[counter][i] != ".":
                    if board[counter][i] in nums_dict:
                        return False
                    else:
                        nums_dict[board[counter][i]] = 1
        for j in range(3):
            j *= 3
            for row in range(3): #checking each box
                nums_dict = dict()
                row *= 3
                for i in range(3):
                    for col in range(3):
                        if board[row + i][col + j] != ".":
                            if board[row + i][col + j] in nums_dict:
                                return False
                            else:
                                nums_dict[board[row + i][col + j]] = 1
        


        return True
        
