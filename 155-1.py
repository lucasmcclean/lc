class MinStack:

    def __init__(self):
      self.stk = []
      self.mins = []

    def push(self, val: int) -> None:
        n = len(self.stk)
        self.stk.append(val)
        if n == 0 or val < self.stk[self.mins[-1]]:
            self.mins.append(n)

    def pop(self) -> None:
        n = len(self.stk)
        if self.mins[-1] == n - 1:
            self.mins.pop()
        self.stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.stk[self.mins[-1]]
