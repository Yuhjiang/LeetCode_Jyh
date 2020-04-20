class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = None
        self.stack = []

    def push(self, x: int) -> None:
        if self.min is None or x < self.min:
            self.min = x
        self.stack.append(x)

    def pop(self) -> None:
        value = self.stack.pop()
        if value == self.min:
            self.refind()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min

    def refind(self) -> None:
        if not self.stack:
            self.min = None
        else:
            self.min = min(self.stack)



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
if __name__ == '__main__':
    obj = MinStack()
    obj.push(2147483646)
    obj.push(2147483646)
    obj.push(2147483647)
    obj.pop()
    obj.pop()
    obj.pop()
    print(obj.stack)
    print(obj.getMin())
    obj.push(2147483647)
    print(obj.getMin())