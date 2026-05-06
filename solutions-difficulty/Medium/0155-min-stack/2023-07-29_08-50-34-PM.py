class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        if not self.minstack or val <= self.minstack[-1]:
            #if the minstack is empty or if the val is less than the most recent val in the min stack, then append the val to minstack
            self.minstack.append(val)
        self.stack.append(val) #append the val to the stack


    def pop(self) -> None:
        if self.minstack[-1] == self.stack[-1]: #if the last element in the minstack is the same as the element we are removing in stack then remove that val from the minstack as well
            self.minstack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1] #the last element will always be the smallest element


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
