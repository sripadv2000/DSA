# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minheap = []
        res = []
        k = len(lists)

        for idx, node in enumerate(lists):
            if node:
                heapq.heappush(minheap, (node.val, idx, node))

        dummy = ListNode(0)
        tail = dummy
        
        while minheap:
            val, index, node = heapq.heappop(minheap)
            tail.next = node
            tail = tail.next

            if node.next:
                heapq.heappush(minheap, (node.next.val, index, node.next))
        
        return dummy.next

