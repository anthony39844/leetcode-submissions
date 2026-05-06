class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        s = []
        ops = {'+' : 0, '-': 0, '*': 0, '/': 0}

        for i in tokens:
            if i not in ops:
                s.append(int(i))
            else:
                x = s.pop()
                y = s.pop()
                if i == '+':
                    s.append(x + y)
                elif i == '-':
                    s.append(y - x)
                elif i == '*':
                    s.append(x * y)
                elif i == '/':
                    s.append(int(y / x))

        return s.pop()
