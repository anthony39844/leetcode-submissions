class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        d = [0] * 26
        for i in s1:
            if i not in s2:
                return False
            d[ord(i) - ord('a')] += 1
        
        d2 = [0] * 26
        s = s2[:len(s1)]
        for i in s:
            d2[ord(i) - ord('a')] += 1

        if d == d2:
            return True
        
        l = 0
        for r in range(len(s1), len(s2)):
            d2[ord(s2[l]) - ord('a')] -= 1
            
            d2[ord(s2[r]) - ord('a')] += 1

            if d2 == d:
                return True
            l += 1

        return False
            
                

