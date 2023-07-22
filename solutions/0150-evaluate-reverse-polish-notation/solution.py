class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        answer = 0
        if len(tokens) == 1: # if the list is only a number just return the number
            return int(tokens[0])
        for i in tokens: #for every value in the list 
            if i != '+' and i != '*' and i != '/' and i != '-':
                stack.append(i)
                #if it is not a operator then append it to the stack
            else:
                x = int(stack.pop()) #else pop the last two elements and perform the operation
                y = int(stack.pop())
                if i == '+':
                    answer = y + x
                elif i == '-':
                    answer = y - x
                elif i == '/':
                    answer = y / x
                elif i == '*':
                    answer = y * x
                stack.append(answer) #append the new answer to the stack
        return int(stack.pop())

