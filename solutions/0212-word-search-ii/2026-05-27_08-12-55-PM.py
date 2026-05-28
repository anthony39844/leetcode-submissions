class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        cur = self.root
        for i in word:
            if i not in cur:
                cur[i] = {}
            cur = cur[i]
            
        cur["end"] = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        out = set()
        def dfs(r, c, node):
            if "end" in node:
                out.add(node["end"])
                del node["end"]

            temp, board[r][c] = board[r][c], "#"
            for x, y in directions:
                a, b = r + x, c + y
                if a >= 0 and a < len(board) and b >= 0 and b < len(board[a]) and board[a][b] in node:
                    dfs(a, b, node[board[a][b]])
            board[r][c] = temp

        trie = Trie()
        for word in words:
            trie.insert(word)
                
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] in trie.root:
                    dfs(i, j, trie.root[board[i][j]])
        
        return list(out)

