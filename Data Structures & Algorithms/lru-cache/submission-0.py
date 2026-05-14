class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next, self.prev = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
    
    def insert(self, node):
        prev = self.right.prev
        prev.next, node.prev = node, prev
        self.right.prev, node.next = node, self.right 

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1        

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if node:
            self.remove(node)
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        if self.capacity < len(self.cache):
            key = self.left.next.key
            self.remove(self.left.next)
            del self.cache[key]


        
