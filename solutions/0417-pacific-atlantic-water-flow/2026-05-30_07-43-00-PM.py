class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        out = set()

        pac_edge, atl_edge = set(), set()
        pac = set()
        for i in range(m):
            for j in range(n):
                if j == 0 or i == 0:
                    pac_edge.add((i, j))
                if i == m - 1 or j == n - 1:
                    atl_edge.add((i, j))

        def dfs(i, j):
            
            out.add((i, j))
            for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                a, b = i + x, j + y
                if (0 <= a < m and 0 <= b < n) and heights[a][b] >= heights[i][j] and (a, b) not in out:
                    dfs(a, b)

        for x, y in pac_edge:
            dfs(x, y)
        pac = out

        out = set()
        for x, y in atl_edge:
            dfs(x, y)
        atl = out
        out = set()

        for i in pac:
            if i in atl:
                out.add(i)

        return list(out)
