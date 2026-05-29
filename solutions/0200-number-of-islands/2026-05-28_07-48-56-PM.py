class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        out = 0
        
        def dfs(x, y):
            if not (0 <= x < len(grid) and 0 <= y < len(grid[x])):
                return
            if grid[x][y] != "1":
                return

            grid[x][y] = "#"
            for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                dfs(x + i, y + j)
            
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    out += 1

        return out
