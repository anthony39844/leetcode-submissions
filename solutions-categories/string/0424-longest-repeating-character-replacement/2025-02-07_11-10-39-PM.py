class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        out = 0
        l = 0
        x = 0
        count = defaultdict(int)
        for i in range(0, len(s)):
            count[s[i]] += 1
            x = (i - l + 1) - max(count.values()) #how many characters need to be changed
            if x > k: #if greater, move the window up, update count
                count[s[l]] -= 1
                l += 1
            out = max(out, i - l + 1) #get length of window

        return out

