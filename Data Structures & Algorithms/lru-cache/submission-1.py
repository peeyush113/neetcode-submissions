class Node:

    def __init__(self, key=None, val=None, next=None, prev=None) -> None:

        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node(prev=self.head)
        self.head.next = self.tail
        self.hash = {}
        self.capacity = capacity
        self.currCap = 0

    def remove_node(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
    
    def insert(self, node):
        node.next, node.prev = self.head.next, self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.hash:
            return -1

        node = self.hash[key]
        self.remove_node(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            node = self.hash[key]
            node.val = value
            self.remove_node(node)
        else:
            node = Node(key, value)
            self.hash[key] = node
            self.currCap += 1
        
        self.insert(node)
        if self.currCap > self.capacity:
            lru_node = self.tail.prev
            del self.hash[lru_node.key]
            self.remove_node(lru_node)
            self.currCap -= 1

