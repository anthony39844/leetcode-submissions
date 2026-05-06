class Solution:
    def isPalindrome(self, s: str) -> bool:
        stack = []
        s = s.lower()
        for i in s:
            if i.isalnum():
                stack.append(i)
                
        for i in s:
            if i.isalnum() and i != stack.pop():
                return False

        return True

