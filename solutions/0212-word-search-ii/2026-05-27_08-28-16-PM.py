class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            node = trie
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node["end"] = word  

        rows, cols = len(board), len(board[0])
        res = []

        def dfs(r, c, parent):
            char = board[r][c]
            node = parent[char]
            
            # prune word from trie
            if "end" in node:
                res.append(node["end"])
                del node["end"] 

            cur, board[r][c] = board[r][c], "#"

            for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                a, b = r + x, c + y
                if 0 <= a < rows and 0 <= b < cols:
                    if board[a][b] in node:
                        dfs(a, b, node)

            board[r][c] = cur

            # if this letter has no children, remove it from the trie
            if not node:
                del parent[char]

        for i in range(rows):
            for j in range(cols):
                if board[i][j] in trie:
                    dfs(i, j, trie)

        return res
