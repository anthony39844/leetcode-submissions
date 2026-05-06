class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        s = set()
        for i in board: #rows
            s.clear()
            for j in i:
                if j in s and j != ".":
                    return False
                else:
                    s.add(j)
    
        for i in range(len(board)):
            s.clear()
            for j in range(len(board)):
                p = board[j][i]
                if p in s and p != ".":
                    return False
                else:
                    s.add(p)

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                s.clear()
                for a in range(i, i + 3):
                    for b in range(j, j + 3):
                        p = board[a][b]
                        if p in s and p != ".":
                            return False
                        else:
                            s.add(p)
                            
        return True


     
