class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()
        start = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    start.append((i, j))

        def dfs(r, c, idx):
            if idx == len(word):
                return True
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                return False
            if board[r][c] != word[idx] or (r, c) in visited:
                return False

            visited.add((r, c))
            for x, y in directions:
                a, b = r + x, c + y
                if dfs(a, b, idx + 1):
                    return True
            visited.remove((r, c))

        for x, y in start:
            if dfs(x, y, 0):
                return True
        
        return False

