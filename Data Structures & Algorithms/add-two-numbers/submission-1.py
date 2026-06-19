# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr = head
        
        carry = 0
        while l1 or l2:
            a = carry
            if l1:
                a += l1.val
                l1 = l1.next
            
            if l2:
                a += l2.val
                l2 = l2.next
            
            carry = a//10
            print(a, carry)
            curr.next = ListNode(a%10)
            curr = curr.next
            a = 0
        if carry:
            curr.next = ListNode(carry)
        return head.next
