class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #rows
        s = set()
        for i in range(len(board)):
            s.clear()
            for j in board[i]:
                if j not in s or j == ".":
                    s.add(j)
                else:
                    return False

        #columns
        for i in range(len(board)):
            s.clear()
            for j in range(len(board)):
                if board[j][i] not in s or board[j][i] == ".":
                    s.add(board[j][i])
                else:
                    return False

        #boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                s.clear()
                for x in range(3):
                    for y in range(3):
                        piece = board[j + x][i + y]
                        if piece not in s or piece == ".":
                            s.add(piece)
                        else:
                            return False
        
        return True

     
