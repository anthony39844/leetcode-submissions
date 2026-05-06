# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        cur = head
        while cur:
            cur = cur.next
            count += 1

        cur = head
        prev = None
        for i in range(count - n):
            prev = cur
            cur = cur.next
        
        print(cur, prev)
        if prev:
            if cur.next:
                prev.next = cur.next
            elif cur:
                prev.next = None
        else:
            if cur.next:
                head = cur.next
            else:
                return None
        return head
