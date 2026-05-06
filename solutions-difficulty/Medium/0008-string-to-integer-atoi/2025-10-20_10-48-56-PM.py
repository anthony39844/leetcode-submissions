class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0

        MAX = (2 ** 31) - 1
        MIN = -2 ** 31
        sign = 1
        i = 0

        if s[i] == "+":
            i += 1
        elif s[i] == "-":
            i += 1
            sign = -1

        out = 0    
        while i < len(s) and s[i].isdigit():
            out = out * 10 + int(s[i])
            i += 1

        if out == 0:
            return 0
        else:
            x = sign * out
            if x > MAX:
                return MAX
            elif x < MIN:
                return MIN
            else:
                return x
        
        
    
