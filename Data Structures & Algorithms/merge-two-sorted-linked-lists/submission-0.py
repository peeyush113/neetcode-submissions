# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode()
        l1 = list1
        l2 = list2
        node = head
        while l1 and l2:
            if l1.val <= l2.val:
                tmp = l1.next
                l1.next = None
                node.next = l1
                l1 = tmp
            else:
                tmp = l2.next
                l2.next = None
                node.next = l2
                l2 = tmp
            node = node.next
        
        while l1:
            tmp = l1.next
            l1.next = None

            node.next = l1

            l1 = tmp
            node = node.next

        while l2:
            tmp = l2.next
            l2.next = None

            node.next = l2

            l2 = tmp
            node = node.next
        
        return head.next