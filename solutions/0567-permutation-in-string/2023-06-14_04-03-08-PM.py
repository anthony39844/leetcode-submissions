class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        
        d1 = {c:0 for c in string.ascii_lowercase}
        d2 = {c:0 for c in string.ascii_lowercase}

        for i in s1:
            d1[i] += 1

        for j in range(len(s2)):
            d2[s2[j]] += 1
            if j >= len(s1):
                d2[s2[j - len(s1)]] -= 1
            if(d1 == d2):
                return True
        
        return False
"""
        window = len(s1)
        left = 0
        right = left + window - 1
        letters = {}
        substring = {}
        for c in s1:
            substring[c] = 1 + substring.get(c, 0)
        while right < len(s2):
            letters.clear()
            for i in s2[left: right + 1]:
                letters[i] = 1 + letters.get(i, 0)
            if substring == letters:
                return True

            left += 1
            right = left + window - 1
        return False
"""

