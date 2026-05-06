class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        letterCount = {}
        for char in s:
            if char not in letterCount:
                letterCount[char] = 1
            else:
                letterCount[char] += 1

        for char in t:
            if char not in letterCount or (t.count(char) != letterCount[char]) :
                return False

        return True
        
