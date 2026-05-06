class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        out = 0
        l = 0
        x = 0
        count = {}
        for i in range(0, len(s)):
            count[s[i]] = count.get(s[i], 0) + 1
            x = (i - l + 1) - max(count.values())
            if x > k:
                count[s[l]] -= 1
                l += 1
            out = max(out, i - l + 1)
            # if s[i] != s[l]:
            #     x += 1
            #     if x > k:

            #         while s[i] != s[l]:
            #             l += 1
            #         x -= 1
            # out = max(out, i - l + 1)
            # print(x, l, i, out, count)

   
        return out

