class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        e = {}
        for i in s:
            d[i] = d.get(i, 0) + 1

        for i in t:
            e[i] = e.get(i, 0) + 1
        
        if e == d:
            return True
        else:
            return False
