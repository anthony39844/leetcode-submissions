class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        left, right = 0, 1
        d = dict()
        count = 0
        while right < len(s): 
            d[s[left]] = left
            if s[right] not in d:
                d[s[right]] = right
                right += 1
            else:
                count = max(count, len(d))
                left = d[s[right]] + 1
                right = left + 1
                d = {}

        count = max(count, len(d))

        return count
