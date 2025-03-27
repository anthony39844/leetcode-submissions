class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        d2 = {}

        for i in s:
            d[i] = d.get(i, 0) + 1
        
        for i in t:
            d2[i] = d2.get(i, 0) + 1
        
        if d == d2:
            return True
        return False
