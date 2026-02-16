# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        leftPre = dummy
        curNode = head

        for i in range(0, left-1):
            leftPre = leftPre.next
            curNode = curNode.next

        # Marker to the node where we start reversing
        subListHead = curNode

        preNode = None
        for i in range(0, right-left+1):
            nextNode = curNode.next
            curNode.next = preNode
            preNode = curNode
            curNode = nextNode
        
        # Join the pieces
        leftPre.next = preNode
        subListHead.next = curNode

        return dummy.next


