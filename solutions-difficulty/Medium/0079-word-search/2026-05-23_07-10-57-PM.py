class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        # Optimization 1: Frequency Check Pruning
        # If the board doesn't have enough characters to even build the word, exit early.
        board_counts = Counter(char for row in board for char in row)
        word_counts = Counter(word)
        
        for char, count in word_counts.items():
            if board_counts[char] < count:
                return False

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c, idx):
            if idx == len(word):
                return True
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                return False
            if board[r][c] != word[idx]:
                return False

            # instead of using a visited set, we replace the current char with # in place
            # saves memory and we can just replace it after
            temp, board[r][c] = board[r][c], "#"
            for x, y in directions:
                a, b = r + x, c + y
                if dfs(a, b, idx + 1):
                    return True
            board[r][c] = temp

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        
        return False

