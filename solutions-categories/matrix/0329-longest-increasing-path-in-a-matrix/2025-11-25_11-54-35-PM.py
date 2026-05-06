class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        direct = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        longest = 0

        @cache
        def dfs(x, y):
            m = 0
            for dx, dy in direct:
                if x + dx >= len(matrix) or x + dx < 0 or y + dy >= len(matrix[0]) or y + dy < 0:
                    continue
                if matrix[x+dx][y+dy] > matrix[x][y]:
                    m = max(dfs(x+dx, y+dy), m)
            
            return m + 1
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                longest = max(longest, dfs(i, j))
        
        return longest
