# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        slow, fast = head, head
        ptr = None

        while fast != None and fast.next != None:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = slow.next
        del slow

        return head