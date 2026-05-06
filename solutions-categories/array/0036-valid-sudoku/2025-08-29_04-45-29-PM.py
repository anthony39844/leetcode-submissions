class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows
        s = set()
        for row in board:
            s.clear()
            for x in row:
                if x not in s:
                    s.add(x)
                elif x != ".":
                    return False
        # cols
        for i in range(len(board)):
            s.clear()
            for j in range(len(board)):
                if board[j][i] not in s:
                    s.add(board[j][i])
                elif board[j][i] != ".":
                    return False

        # sqaures
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                s.clear()
                for a in range(3):
                    for b in range(3):
                        x = board[a + i][b + j]
                        if x not in s:
                            s.add(x)
                        elif x != ".":
                            return False

        return True

