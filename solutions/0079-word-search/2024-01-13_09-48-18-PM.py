class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, k):
            if not (0 <= i < len(board)) or not (0 <= j < len(board[0])) or board[i][j] != word[k]:
                return False

            if k == len(word) - 1:
                return True

            temp, board[i][j] = board[i][j], '/'
            result = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            board[i][j] = temp

            return result

        for row in range(len(board)):
            for col in range(len(board[0])):
                if dfs(row, col, 0):
                    return True

        return False
        
