class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = Node(0)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        node = self.head.next
        for i in range(index):
            if not node:
                return -1
            node = node.next
        if not node:
            return -1
        return node.val


    def insertHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head.next
        self.head.next = node

        if self.tail == self.head:
            self.tail = node

    def insertTail(self, val: int) -> None:
        node = Node(val)
        self.tail.next = node
        self.tail = node

    def remove(self, index: int) -> bool:
        prev = self.head
        curr = self.head.next
        
        while curr:
            if index == 0:
                prev.next = curr.next
                if curr == self.tail:
                    self.tail = prev
                return True
            
            prev = curr
            curr = curr.next
            index -= 1
        return False

    def getValues(self) -> List[int]:
        op = []
        curr = self.head.next
        while curr:
            op.append(curr.val)
            curr = curr.next
        return op
        
