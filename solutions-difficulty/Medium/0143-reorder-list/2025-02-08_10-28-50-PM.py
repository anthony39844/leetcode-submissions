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

        back, end = head, head.next

        while end and end.next:
            back = back.next
            end = end.next.next

        node = back.next

        back.next = None

        cur, prev = node, None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        
        back = prev
        front = head
        b_next = back
        print(back)

        
        while back:
            next = front.next
            front.next = b_next
            front = next

            b_next = back.next
            back.next = next
            back = b_next




