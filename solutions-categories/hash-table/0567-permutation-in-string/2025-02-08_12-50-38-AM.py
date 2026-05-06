class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        d = {}
        for i in s1:
            if i not in s2:
                return False
            d[i] = d.get(i, 0) + 1
        
        d2 = {}
        s = s2[:len(s1)]
        for i in s:
            d2[i] = d2.get(i, 0) + 1

        if d == d2:
            return True
        
        l = 0
        for r in range(len(s1), len(s2)):
            d2[s2[l]] -= 1
            if d2[s2[l]] == 0:
                del d2[s2[l]]
            
            d2[s2[r]] = d2.get(s2[r], 0) + 1

            if d2 == d:
                return True
            l += 1

        return False
            
                

