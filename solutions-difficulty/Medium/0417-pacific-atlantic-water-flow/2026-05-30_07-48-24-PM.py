class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        out = set()
        pac, atl = set(), set()

        def dfs(i, j, ocean):
            ocean.add((i, j))
            for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                a, b = i + x, j + y
                if (0 <= a < m and 0 <= b < n) and heights[a][b] >= heights[i][j] and (a, b) not in ocean:
                    dfs(a, b, ocean)

        # top and bottom borders
        for i in range(n):
            dfs(0, i, pac)
            dfs(m - 1, i, atl)

        # left and right borders
        for i in range(m):
            dfs(i, 0, pac)
            dfs(i, n - 1, atl)

        for i in pac:
            if i in atl:
                out.add(i)

        return list(out)
