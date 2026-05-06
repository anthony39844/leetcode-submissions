class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []    
        def generate(o, c, s, out):
            if len(s) == n * 2:
                out.append(s)
                return
            if o < n: 
                generate(o + 1, c, s + "(", out)
            if c < n and c < o:
                generate(o, c + 1, s + ")", out)

        generate(1, 0, "(", stack)
        return stack

