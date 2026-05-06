class Solution:
    def longestPalindrome(self, s: str) -> str:
        res1 = ""
        res2 = ""
        for i in range(len(s)):
            l, r = 0, 0
            while i + r < len(s) and i - l >= 0 and s[i - l] == s[i + r]:
                l += 1
                r += 1
            if 2 * r > len(res1):
                res1 = s[i-l+1:i+r]

            if i + 1 < len(s) and s[i] == s[i + 1]:
                l, r = 0, 0
                while i - l >= 0 and i + 1 + r < len(s) and s[i - l] == s[i + 1 + r]:
                    print(i, l, r)
                    l += 1
                    r += 1
            
                if 2 * r + 1 > len(res2):
                    print("longer pal")
                    res2 = s[i-l+1:i+1+r]

        return res1 if len(res1) > len(res2) else res2
        
            
