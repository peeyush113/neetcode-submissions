# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        resp = ListNode(0)
        curr = resp

        while True:
            minNode = None
            for i in range(len(lists)):
                if lists[i] is not None:
                    if minNode is None or lists[i].val < lists[minNode].val:
                        minNode = i
            
            if minNode is None:
                break
            
            curr.next, lists[minNode] = lists[minNode], lists[minNode].next
            curr = curr.next
        return resp.next

