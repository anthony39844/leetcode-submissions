class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out = []

        def generate(o, c, s):
            if len(s) == n * 2:
                out.append(s)
                return 
            if o < n:
                generate(o + 1, c, s + "(")
            if c < o:
                generate(o, c + 1, s + ")")
    
        generate(0, 0, "")
        return out
            
