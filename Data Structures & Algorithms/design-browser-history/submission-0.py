class Node:
    def __init__(self, url="", next=None, back=None) -> None:
        self.url:str = url 
        self.next: Node|None = next
        self.back: Node| None = back

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.curr = self.head

    def visit(self, url: str) -> None:
        self.curr.next = Node(url, None, self.curr)
        self.curr = self.curr.next

    def back(self, steps: int) -> str:
        while steps>0 and self.curr.back:
            self.curr = self.curr.back
            steps -= 1
        return self.curr.url

    def forward(self, steps: int) -> str:
        while steps>0 and self.curr.next:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)