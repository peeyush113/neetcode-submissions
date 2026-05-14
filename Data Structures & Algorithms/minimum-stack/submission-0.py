class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        minVal = min(self.getMin(), val)
        self.minStack.append(minVal)

    def pop(self) -> None:
        v = self.stack.pop()
        self.minStack.pop()
        return

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.minStack) > 0:
            return self.minStack[-1]
        return float('inf')   
