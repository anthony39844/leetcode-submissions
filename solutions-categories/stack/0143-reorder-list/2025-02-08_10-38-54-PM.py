# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next or not head.next.next:
            return

        back, end = head, head.next

        while end and end.next: #using slow and fast pointer to find middle of list
            back = back.next
            end = end.next.next

        cur = back.next #back end of the list
        back.next = None #

        prev = None #reversing list
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        
        back = prev
        front = head
        b_next = back

        while back:
            next = front.next
            front.next = b_next
            front = next

            b_next = back.next
            back.next = next
            back = b_next




