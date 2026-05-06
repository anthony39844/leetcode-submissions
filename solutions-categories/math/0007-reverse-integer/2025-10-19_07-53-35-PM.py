class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x < 0:
            neg = True
        x = abs(x)
        length = len(str(x))
        out = 0
        while x > 0:
            out += (x % 10) * (10 ** (length - 1))
            x = x // 10
            length -= 1

        
        # count = len(digits)
        # for i in digits:
        #     print(10**(count-1), i)
        #     out += (10 ** (count-1)) * i
        #     count -= 1
        
        out = out if not neg else out * -1
        if out > (2 ** 31) - 1 or out < -2 ** 31:
            return 0
        else:
            return out
        
        
