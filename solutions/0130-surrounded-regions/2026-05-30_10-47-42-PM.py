class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        def dfs(i, j):
            board[i][j] = "END"
            for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                a, b = i + x, j + y
                if (0 <= a < m and 0 <= b < n) and board[a][b] == "O":
                    dfs(a, b)

        for i in range(n):
            if board[0][i] == "O":
                dfs(0, i)
            if board[m-1][i] == "O":
                dfs(m - 1, i)
        
        for i in range(m):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][n-1] == "O":
                dfs(i, n - 1)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "END":
                    board[i][j] = "O"
