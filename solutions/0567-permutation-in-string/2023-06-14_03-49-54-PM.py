class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
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

