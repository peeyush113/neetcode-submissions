# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def ll(l):
    resp = "->"
    while l:
        resp += f"{l.val}->"
        l = l.next
    return resp


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        cur = slow.next
        slow.next = None

        print("1", ll(fast), ll(slow), ll(head), ll(cur))
        prev = None
        while cur:
            print("2", ll(cur), ll(prev))
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
            print("3", ll(cur), ll(prev), ll(tmp))

        node = head
        while prev and node:
            print("4", ll(cur), ll(node))
            tmp = prev.next
            prev.next = node.next
            node.next= prev
            node = prev.next
            prev = tmp
            
                