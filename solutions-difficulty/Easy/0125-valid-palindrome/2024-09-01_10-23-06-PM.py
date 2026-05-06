class Solution:
    def isPalindrome(self, s: str) -> bool:
        stack = []
        s = s.lower()
        for i in s:
            if i.isalnum():
                stack.append(i)

        if not stack:
            return True
            
        for i in s:
            if i.isalnum():
                a = stack.pop()
                if i != a:
                    return False
        
        return True
