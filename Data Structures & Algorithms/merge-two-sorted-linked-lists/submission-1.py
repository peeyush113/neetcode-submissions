# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
            
        head = ListNode()
        curr = head
        while list1 and list2:
            if list1.val <= list2.val:
                tmp = list1.next
                list1.next = None
                curr.next = list1
                list1 = tmp
            elif list2.val <= list1.val:
                tmp = list2.next
                list2.next = None
                curr.next = list2
                list2 = tmp
            else:
                pass
            curr = curr.next            
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2
        return head.next
