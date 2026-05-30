class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        out = 0
        m, n = len(grid), len(grid[0])
        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))

        while q:
            for i in range(len(q)):
                x, y = q.popleft()
                for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    a, b = x + i, y + j
                    if (0 <= a < m and 0 <= b < n) and grid[a][b] == 1:
                        grid[a][b] = 2
                        q.append((a, b))
            if len(q) > 0:
                out += 1
        
        for i in grid:
            if 1 in i:
                return -1

        return out
