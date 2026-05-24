class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out = []

        def backtrack(s, openp, closep):
            if len(s) == n * 2:
                out.append(s)
                return
            
            if openp < n:
                backtrack(s + "(", openp + 1, closep)
            
            if openp > closep:
                backtrack(s + ")", openp, closep + 1)


        backtrack("", 0, 0)
        return out
