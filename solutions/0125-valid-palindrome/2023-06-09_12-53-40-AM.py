class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left = 0
        right = len(s) - 1
        while left < right:
            if not s[left].isalpha() and not s[left].isdigit():
                left += 1
            elif not s[right].isalpha() and not s[right].isdigit():
                right -= 1
            elif s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True

      
            
