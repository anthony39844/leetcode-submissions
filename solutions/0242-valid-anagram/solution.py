class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = dict()
        d2 = dict()
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            d[s[i]] = d.get(s[i], 0) + 1
            d2[t[i]] = d2.get(t[i], 0) + 1
        
        return d == d2
        
