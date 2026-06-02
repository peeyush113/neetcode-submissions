class MyStack:

    def __init__(self):
        self.q = deque()
        self.p = deque()

    def push(self, x: int) -> None:
        self.p.append(x)
        while self.q:
            self.p.append(self.q.popleft())
        self.p, self.q = self.q, self.p

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) ==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()