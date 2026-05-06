class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []    
        def generate(o, c, s):
            if len(s) == n * 2:
                stack.append(s)
                return
            if o < n: 
                generate(o + 1, c, s + "(")
            if c < o:
                generate(o, c + 1, s + ")")

        generate(1, 0, "(")
        return stack

