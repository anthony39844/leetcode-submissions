class MinStack:

    def __init__(self):
        self.s = []
        self.min_s = []

    def push(self, val: int) -> None:
        if not self.min_s or self.min_s[-1] >= val:
            self.min_s.append(val)
        print(self.min_s)
        self.s.append(val)

    def pop(self) -> None:
        x = self.s.pop()
        if x == self.min_s[-1]:
            self.min_s.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.min_s[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
