class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        while n > 2:
            n = n / 2
        if n % 2 == 0:
            return True
        return False
