class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = ['(', '{', '[']
        d = {'(' : ')', '{' : '}', '[' : ']'}
        for i in s:
            if i in open:
                stack.append(d[i])
            else:
                if stack:
                    a = stack.pop()
                    if i != a:
                        return False
                else:
                    return False
        if stack == []:
            return True
        else:
            return False
