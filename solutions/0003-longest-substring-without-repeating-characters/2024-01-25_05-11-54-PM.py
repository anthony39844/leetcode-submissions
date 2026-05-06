class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1

        # left, count = 0, 0
        # d = dict()
        # for i, c in enumerate(s):
        #     if d.get(c, -1) >= left:
        #         left = d[c] + 1
        #     count = max(count, i - left + 1)
        #     d[c] = i

        # return count
        left, right, count = 0, 1, 0
        d = dict()
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

