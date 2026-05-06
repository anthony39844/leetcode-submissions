class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        '''
        
        '''
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        out = [0] * (m + n)
        num1_digits = [ord(c) - 48 for c in num1]
        num2_digits = [ord(c) - 48 for c in num2]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                p1, p2 = i + j, i + j + 1
                s = num1_digits[i] * num2_digits[j] + out[p2]
                out[p2] = s % 10
                out[p1] += s // 10

        # Skip leading zeros manually
        start = 0
        while start < len(out) - 1 and out[start] == 0:
            start += 1

        return ''.join(map(str, out[start:]))
