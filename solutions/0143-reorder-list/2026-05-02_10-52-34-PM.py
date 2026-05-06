# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        cur = head
        s = []
        x = 0
        
        while cur:
            s.append(cur)
            cur = cur.next
            x += 1

        half = math.ceil(x / 2)

        for i in range(half - 1):
            head.next = s.pop()
            head = head.next
            head.next = None

            head.next = s[i + 1]
            head = head.next
            head.next = None

        if x % 2 == 0:
            head.next = s.pop()
            head = head.next
            head.next = None


