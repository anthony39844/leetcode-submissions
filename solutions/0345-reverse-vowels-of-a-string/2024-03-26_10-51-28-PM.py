class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        d = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] in d and s[right] in d:
                temp = s[left]
                s[left] = s[right]
                s[right] = temp
                left += 1
                right -= 1
            elif s[left] in d:
                right -= 1
            else:
                left += 1
        return "".join(s)

