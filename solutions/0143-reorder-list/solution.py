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
        back.next = None #severs front of list from the back half, otherwise when reversing back will point to the last node in the rev list

        prev = None #reversing list
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        
        front = head
        b_next = prev

        while prev:
            next = front.next
            front.next = b_next
            front = next

            b_next = prev.next
            prev.next = next
            prev = b_next




