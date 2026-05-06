class Solution:
    def reverse(self, x: int) -> int:
        OVERFLOW_NEG = -2 ** 31
        OVERFLOW_POS = (2 ** 31) - 1
        neg = False
        if x < 0:
            neg = True
        x = abs(x)
        length = len(str(x))
        out = 0
        while x > 0:
            out += (x % 10) * (10 ** (length - 1))
            if out > OVERFLOW_POS or out * -1 < OVERFLOW_NEG:
                return 0
            x = x // 10
            length -= 1
        
        out = out if not neg else out * -1
        return out
        
        
