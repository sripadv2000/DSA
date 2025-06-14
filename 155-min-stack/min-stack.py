class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        if len(self.minStack) == 0 or val <= self.minStack[-1]:
            self.minStack.append(val)
        return self.stack.append(val)

    def pop(self) -> None:
        poping_element = self.stack[-1]
        if self.minStack and self.minStack[-1] == poping_element:
            self.minStack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()