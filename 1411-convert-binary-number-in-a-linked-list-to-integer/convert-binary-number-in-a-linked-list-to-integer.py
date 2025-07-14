# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        length = 0
        temp = head
        while temp != None:
            temp = temp.next
            length += 1
        ans = 0
        length = length - 1
        while head != None:
            ans += (head.val) * (1 << length)
            length = length - 1
            head = head.next
        return ans
        