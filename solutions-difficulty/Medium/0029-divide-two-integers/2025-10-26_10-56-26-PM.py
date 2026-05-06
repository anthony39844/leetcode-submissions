import math
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == divisor:
            return 1
        MIN = -2 ** 31
        MAX = (2 ** 31) - 1
        x = abs(divisor)
        y = abs(dividend)
        isNeg = (dividend < 0) != (divisor < 0)
        out = 0

        # shift divisor over 1 bit until number is bigger than dividend
        # subtract that value from the dividen
        # repeat this until the divisor is bigger than the remaining value

        while x <= y:
            count = 0
            while y > x << (count + 1):
                count += 1
            y -= x << count
            out += 1 << count
            
        out = out if not isNeg else -out
        if out > MAX:
            return MAX
        elif out < MIN:
            return MIN
        else:
            return out

