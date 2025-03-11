class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        ops = ["+", "-", "*", "/"]
        for i in tokens:
            if i not in ops:
                s.append(i)
            else:
                x = int(s.pop())
                y = int(s.pop())
                if i == "+":
                    s.append(x + y)
                elif i == "-":
                    s.append(y - x)
                elif i == "*":
                    s.append(x * y)
                elif i == "/":
                    s.append(math.trunc(y / x))
        
        return int(s.pop())
            

