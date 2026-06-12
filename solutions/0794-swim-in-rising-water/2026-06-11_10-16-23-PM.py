class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        heap = [(grid[0][0], 0, 0)]
        out = 0
        visited = {(0, 0)}

        while True:
            val, x, y = heapq.heappop(heap)
            out = max(out, val)
        
            if x == m - 1 and y == n - 1:
                return out
            for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                a, b = x + i, y + j
                if (a, b) not in visited and (0 <= a < m and 0 <= b < n):
                    heapq.heappush(heap, (grid[a][b], a, b))
                    visited.add((a, b))
        
