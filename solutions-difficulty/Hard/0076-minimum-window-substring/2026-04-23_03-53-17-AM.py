class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""
        
        if s == t:
            return s

        # d1 = baseline, d2 = current window
        d1 = {}
        d2 = {}
        for i in range(len(t)):
            d1[t[i]] = d1.get(t[i], 0) + 1

        matches = 0     
        min_len = float('inf')
        start, end = 0, 0
        l, r = 0, 0

        while r < len(s):
            if s[r] in t:
                d2[s[r]] = d2.get(s[r], 0) + 1
                if d2[s[r]] == d1[s[r]]:
                    matches += 1

            # when we have a valid substring, update indexes, loop until next valid char
            while l < len(s) and matches == len(d1.keys()):
                if s[l] in t:
                    if (r + 1) - l < min_len:
                        start = l
                        end = r + 1
                        min_len = (r + 1) - l
                    d2[s[l]] -= 1
                    if d2[s[l]] < d1[s[l]]:
                        matches -= 1
                l += 1

            r += 1
  
        return s[start:end]


