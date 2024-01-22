class MinStack:

    def __init__(self):
        self.list = []
        self.count = 0
        self.minlist = []

    def push(self, val: int) -> None:
        if not self.minlist or val <= self.minlist[-1]:
            self.minlist.append(val)
        self.list.append(val)
        self.count += 1

    def pop(self) -> None:
        if self.count > 0:
            remove = self.list.pop(self.count - 1)
            if remove == self.minlist[-1]:
                self.minlist.pop()
            self.count -= 1

    def top(self) -> int:
        return self.list[self.count - 1]

    def getMin(self) -> int:
        if len(self.list) == 0:
            return None
        return self.minlist[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
