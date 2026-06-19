# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr = head
        
        while list1 and list2:
            if list1.val > list2.val:
                list1, list2 = list2, list1
            
            tmp = list1.next
            list1.next = None
            curr.next = list1
            list1 = tmp
            curr = curr.next
        
        while list1:
            tmp = list1.next
            list1.next = None
            curr.next = list1
            list1 = tmp
            curr = curr.next
        while list2:
            tmp = list2.next
            list2.next = None
            curr.next = list2
            list2 = tmp
            curr = curr.next

        return head.next