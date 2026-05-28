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
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                return 
            if board[r][c] not in node:
                return

            temp, board[r][c] = board[r][c], "#"
            for x, y in directions:
                a, b = r + x, c + y
                dfs(a, b, node[temp])
            board[r][c] = temp

        trie = Trie()
        for word in words:
            trie.insert(word)
                
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] in trie.root:
                    dfs(i, j, trie.root)
        
        return list(out)

