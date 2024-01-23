from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowdict = defaultdict(set)
        coldict = defaultdict(set)
        boxdict = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    box = i//3 * 3 + j//3
                    if board[i][j] in rowdict[i] or board[i][j] in coldict[j] or board[i][j] in boxdict[box]:
                        return False
                    else:
                        rowdict[i].add(board[i][j])
                        coldict[j].add(board[i][j])
                        boxdict[box].add(board[i][j])
        return True

        # s = set()
        # for i in range(9):
        #     for j in range(9):
        #         if board[i][j] != '.':
                    
        #             if board[i][j] not in s:
        #                 s.add(board[i][j])
        #             else:
        #                 return False
        #     s = set()
        # s = set()
        # for i in range(9):
        #     for j in range(9):
        #         if board[j][i] != '.':
                    
        #             if board[j][i] not in s:
        #                 s.add(board[j][i])
        #             else:
        #                 return False
        #     s = set()   
        # s = set()
        # for i in range(0, 9, 3):
        #     for j in range(0, 9, 3):
        #         for m in range(i, i + 3):
        #             for n in range(j, j + 3):
        #                 if board[m][n] != '.':
        #                     if board[m][n] not in s:
        #                         s.add(board[m][n])
        #                     else:
        #                         return False

        #         s=set()
        # return True
        
        



