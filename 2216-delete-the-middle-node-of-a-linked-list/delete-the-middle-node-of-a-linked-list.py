# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        slow, fast = dummy, dummy

        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        
        slow.next = slow.next.next

        return dummy.next


