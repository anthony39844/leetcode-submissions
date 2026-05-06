# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next and head:
            return head

        prev = None
        cur = head
        pair = cur.next

        while cur.next:
            if prev:
                prev.next = pair
                cur.next = pair.next
                pair.next = cur
            else:
                cur.next = pair.next
                pair.next = cur
                head = pair
            prev = cur
            cur = cur.next
            if cur:
                pair = cur.next
            else:
                break

        return head
