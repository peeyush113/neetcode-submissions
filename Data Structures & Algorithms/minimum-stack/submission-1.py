class MinStack:

    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        minVal = min(self.getMin(), val)
        self.stack.append((val, minVal))
        
    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1][1]
        return float('inf')   
