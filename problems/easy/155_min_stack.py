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


class NewMinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min_stack:
            self.min_stack.append(x)
        else:
            self.min_stack.append(min(x, self.getMin()))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else None


if __name__ == '__main__':
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print(obj.getMin())
    obj.pop()
    print(obj.top())
    print(obj.getMin())