class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
        res = ""
        for i in range(len(s)):
            if len(s) - i < len(res) // 2:
                break
            l, r = 0, 0
            while i + r < len(s) and i - l >= 0 and s[i - l] == s[i + r]:
                l += 1
                r += 1
            if 2 * r > len(res):
                res = s[i-l+1:i+r]

            if i + 1 < len(s) and s[i] == s[i + 1]:
                l, r = 0, 0
                while i - l >= 0 and i + 1 + r < len(s) and s[i - l] == s[i + 1 + r]:
                    l += 1
                    r += 1
            
                if 2 * r + 1 > len(res):
                    res = s[i-l+1:i+1+r]

        return res
            
