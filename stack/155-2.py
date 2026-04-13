class MinStack:

    def __init__(self):
        self.stack = list()
        self.mins = list()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.mins) == 0 or self.stack[self.mins[-1]] > val:
            self.mins.append(len(self.stack) - 1)
        else:
            self.mins.append(self.mins[-1])

    def pop(self) -> None:
        self.mins.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[self.mins[-1]]
