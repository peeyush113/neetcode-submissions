# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class MinHeap:
    def __init__(self):
        self.heap = [0]
    
    def __str__(self):
        resp = [n.val for n in self.heap[1:]]
        return str(resp)

    def push(self, node: ListNode):
        self.heap.append(node)
        i = len(self.heap) -1
        p = i//2
        print(i, p, self, node.val)
        while i > 1 and self.heap[i].val < self.heap[p].val:
            tmp = self.heap[i]
            self.heap[i] = self.heap[p]
            self.heap[p] = tmp
            i = p
            p = i//2
            print(i, p, node.val)
    
    @property
    def size(self):
        return len(self.heap)-1

    def pop(self):
        if len(self.heap) == 1:
            return None
        if len(self.heap) ==2 :
            return self.heap.pop()

        resp = self.heap[1]
        self.heap[1] = self.heap.pop()

        i = 1
        l = 2*i
        while l < len(self.heap):
            r = l+1
            if (r < len(self.heap) 
                    and self.heap[r].val<self.heap[l].val 
                    and self.heap[r].val<self.heap[i].val):
                tmp = self.heap[r]
                self.heap[r] = self.heap[i]
                self.heap[i] = tmp
                i = r
            elif self.heap[l].val < self.heap[i].val:
                tmp = self.heap[l]
                self.heap[l] = self.heap[i]
                self.heap[i] = tmp
                i = l
            else:
                break
            l, r = 2*i, 2*i +1
        return resp



class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = MinHeap()
        
        for head in lists:
            while head:
                heap.push(head)
                head = head.next
            
        resp = ListNode()
        cur = resp
        while heap.size > 0:
            node = heap.pop()
            cur.next = node
            cur = cur.next
        
        return resp.next





