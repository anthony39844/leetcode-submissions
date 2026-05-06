class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out = []
        stack = []

        def backtrack(open, close, s):
            if open == n and close == n:
                out.append(''.join(s))
                return
            if open < n:
                s.append('(')
                backtrack(open + 1, close, s)
                s.pop()

            if open > close:
                s.append(')')
                backtrack(open, close + 1, s)
                s.pop()
        
        backtrack(0, 0, stack)
        return out


