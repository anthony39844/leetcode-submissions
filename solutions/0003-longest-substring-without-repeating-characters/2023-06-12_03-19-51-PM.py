class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letter_set = set()
        left = 0
        length = 0
        for r in range(len(s)):
            while s[r] in letter_set:
                letter_set.remove(s[left])
                left += 1
            letter_set.add(s[r])
            length = max(length, r - left + 1)
        return length

                


