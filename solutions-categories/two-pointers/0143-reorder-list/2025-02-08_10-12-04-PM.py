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
        if not head.next:
            return

        f_cur, front, back, end = head, head, head, head

        while end and end.next:
            f_cur = back
            back = back.next
            end = end.next.next

        f_cur.next = None

        next, cur, prev = back, back, None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        
        back = prev
        f_next = front
        b_next = back
        while front:
            f_next = front.next
            front.next = b_next
            front = f_next

            if front:
                b_next = back.next
                back.next = f_next
                back = b_next


