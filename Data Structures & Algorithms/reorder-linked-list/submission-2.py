# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return head
        slow, fast, curr = head, head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print(slow.val)
        next_half = slow.next
        slow.next = None
        slow = next_half
        stack = []
        while slow:
            tmp = slow
            slow = slow.next
            tmp.next = None
            stack.append(tmp)
        print(stack)

        while len(stack)>0:
            node = stack.pop()
            node.next = curr.next
            curr.next = node
            curr = node.next        
