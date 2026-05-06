class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        s = []
        ops = ['+', '-', '*', '/']

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
                    if y // x < 0 and y % x != 0:
                        s.append((y // x) + 1)
                    else:
                        s.append(y // x)

        return s.pop()
