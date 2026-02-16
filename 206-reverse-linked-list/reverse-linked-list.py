# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        while(head != None):
            stack.append(head.val)
            head = head.next
        
        dummy = ListNode()
        ptr = dummy
        
        while(stack):
            ptr.next = ListNode(stack.pop())
            ptr = ptr.next
        
        return dummy.next