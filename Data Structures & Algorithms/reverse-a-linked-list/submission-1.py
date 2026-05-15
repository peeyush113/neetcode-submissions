# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode()
        while head:
            tmp = head.next
            head.next = newHead.next
            newHead.next = head 
            head = tmp
        return newHead.next