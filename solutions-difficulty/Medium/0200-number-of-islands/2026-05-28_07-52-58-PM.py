class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        out = 0
        m, n = len(grid), len(grid[0])
        
        def dfs(x, y):
            grid[x][y] = "#"
            for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                a, b = x + i, y + j
                if (0 <= a < m and 0 <= b < n) and grid[a][b] == "1":
                    dfs(a, b)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    out += 1

        return out
