class Solution:
    def isValid(self, s: str) -> bool:
        myStack = []
        
        for i in s:
            if i == '(':
                myStack.append(')')
            elif i == '[':
                myStack.append(']')
            elif i =='{':
                myStack.append('}')
            elif not myStack or myStack.pop() != i:
                return False
        return not myStack

            

        
        
