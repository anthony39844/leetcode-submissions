class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for i in tokens:
            if i == "+":
                x = int(s.pop())
                y = int(s.pop())
                s.append(x + y)
            elif i == "-":
                x = int(s.pop())
                y = int(s.pop())
                s.append(y - x)
            elif i == "*":
                x = int(s.pop())
                y = int(s.pop())
                s.append(x * y)
            elif i == "/":
                x = int(s.pop())
                y = int(s.pop())
                s.append(int(y / x))
            else:
                s.append(i)

        return int(s.pop())
