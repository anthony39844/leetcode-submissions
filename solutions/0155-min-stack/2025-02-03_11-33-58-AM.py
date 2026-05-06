class MinStack:

    def __init__(self):
        self.s = []
        self.m = []

    def push(self, val: int) -> None:
        if len(self.m) == 0:
            self.m.append(val)
        else:
            if val <= self.m[-1]:
                self.m.append(val)
        self.s.append(val)

    def pop(self) -> None:
        if self.s.pop() == self.m[-1]:
            self.m.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.m[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
