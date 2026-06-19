# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head

        curr = ListNode(next=head)
        slow, fast = curr, curr

        for i in range(n):
            fast = fast.next
        
        while fast and fast.next:
            slow, fast = slow.next, fast.next
        
        slow.next = slow.next.next

        return curr.next
