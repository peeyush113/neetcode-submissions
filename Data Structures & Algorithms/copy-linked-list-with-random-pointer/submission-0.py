"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hash = defaultdict(lambda: Node(0))
        hash[None] = None

        curr = head
        while curr:
            hash[curr].val = curr.val
            hash[curr].next = hash[curr.next]
            hash[curr].random = hash[curr.random]
            curr = curr.next
        return hash[head] 
