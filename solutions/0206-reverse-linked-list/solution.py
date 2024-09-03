# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        next = head
        prev = None
        while cur:
            next = next.next
            cur.next = prev
            prev = cur
            cur = next
        return prev
