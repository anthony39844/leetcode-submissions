class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        o = {"(" : ")", "{" : "}", "[": "]"}
        for i in s:
            if i in o:
                stack.append(i) 
            else:
                if not stack or i != o[stack.pop()]:
                    return False

        return len(stack) == 0
