class Solution:
    def reverse(self, x: int) -> int:
        '''
        1234024
         123402 4
          12340 2 4
           1234 0 2 4
            123 4 0 2 4
             12 3 4 0 2 4
              1 2 3 4 0 2 4
        
        4000000
        4200000
        42
        4204321
        '''

        digits = []
        neg = False
        if x < 0:
            neg = True
        x = abs(x)
        while x > 0:
            digits.append(x % 10)
            x = x // 10
        
        out = 0
        count = len(digits)
        for i in digits:
            print(10**(count-1), i)
            out += (10 ** (count-1)) * i
            count -= 1
        
        out = out if not neg else out * -1
        if out > (2 ** 31) - 1 or out < -2 ** 31:
            return 0
        else:
            return out
        
        
