class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        count = 0

        if not grid:
            return 0

        def bfs(grid, i, j):
            q = deque([(i, j)])
            visited.add((i, j))
            while q:
                a, b = q.popleft()
                for x, y in directions:
                    newA = a + x
                    newB = b + y
                    if 0 <= newA < len(grid) and 0 <= newB < len(grid[0]) and grid[newA][newB] == "1" and (newA, newB) not in visited:
                        q.append((newA, newB))
                        visited.add((newA, newB))
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(grid, i, j)
                    count += 1
        
        return count

        
            
        

