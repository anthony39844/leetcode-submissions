class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        count = 1
        max_len = 1
        for i in range(1, len(s)):
            if ord(s[i]) == ord(s[i-1]) + 1:
                count += 1
            else:
                count = 1
            max_len = max(max_len, count)
        
        return max_len
