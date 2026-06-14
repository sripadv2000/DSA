# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        stack = []
        maximum = 0

        while(fast != None and fast != None):
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        while(slow!=None):
            maximum = max(maximum, stack.pop()+slow.val)
            slow = slow.next
        return maximum