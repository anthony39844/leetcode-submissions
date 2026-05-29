class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        out = 0
        m, n = len(grid), len(grid[0])
        
        def dfs(x, y):
            grid[x][y] = 0
            area = 1 
    
            for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                a, b = x + i, y + j
                if (0 <= a < m and 0 <= b < n) and grid[a][b] == 1:
                    area += dfs(a, b) 
            return area 
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    out = max(out, dfs(i, j))

        return out
