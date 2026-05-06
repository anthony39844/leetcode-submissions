class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        answer = 0
        if len(tokens) == 1:
            return int(tokens[0])
        for i in tokens:
            if i != '+' and i != '*' and i != '/' and i != '-':
                stack.append(i)
            else:
                x = int(stack.pop())
                y = int(stack.pop())
                if i == '+':
                    answer = y + x
                elif i == '-':
                    answer = y - x
                elif i == '/':
                    answer = y / x
                elif i == '*':
                    answer = y * x
                stack.append(answer)
        return int(answer)

