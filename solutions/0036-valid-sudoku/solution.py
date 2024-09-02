class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        s = set()
        for i in board:
            s.clear()
            for j in i:
                if j != ".":
                    if j in s:
                        return False
                    s.add(j)

        s.clear()
        for i in range(len(board)):
            s.clear()
            for j in range(len(board)):
                if board[j][i] != ".":
                    if board[j][i] in s:
                        return False
                    s.add(board[j][i])

    
        s.clear()
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                s.clear()
                for k in range(3):
                    for l in range(3):
                        cur = board[i + k][j + l]
                        if cur != ".":    
                            if cur in s:
                                return False
                            s.add(cur)
        
        return True
                
        

        
