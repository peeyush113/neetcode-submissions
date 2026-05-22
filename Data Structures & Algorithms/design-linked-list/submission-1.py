class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        curr = self.head
        while curr:
            if index == 0:
                return curr.val
            index -= 1
            curr = curr.next        
        return -1
            

    def addAtHead(self, val: int) -> None:
        self.head = Node(val, self.head)

    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.head = Node(val)
            return

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= 0:
            self.addAtHead(val)
            return
        curr = self.head
        while curr:
            if index == 1:
                curr.next = Node(val, curr.next)
                return
            curr = curr.next
            index -= 1 

    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return
        if index == 0:
            self.head = self.head.next
            return
        curr = self.head
        while curr and curr.next:
            if index == 1:
                curr.next = curr.next.next
                return
            curr = curr.next
            index -= 1