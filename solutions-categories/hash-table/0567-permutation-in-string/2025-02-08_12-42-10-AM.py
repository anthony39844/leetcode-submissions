class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        d = {}
        for i in s1:
            if i not in s2:
                return False
            d[i] = d.get(i, 0) + 1
        
        l = 0
        x = 0
        cur = 0
        for r in range(len(s1), len(s2) + 1):
            if s2[l] not in d:
                l += 1
                continue
            s = s2[l:r]
            d2 = {}
            for i in s:
                d2[i] = d2.get(i, 0) + 1
            if d == d2:
                return True
            l += 1

        return False
            
                

