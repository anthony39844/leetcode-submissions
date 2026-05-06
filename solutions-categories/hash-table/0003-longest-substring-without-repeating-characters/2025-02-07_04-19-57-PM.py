class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l, r = 0, 1
        x = 1
        se = {s[l]}
        while r < len(s):
            if s[r] in se:
                l += 1
                r = l + 1
                se = {s[l]}
            else:
                se.add(s[r])
                r += 1
            x = max(len(se), x)
        return x
            
