# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # reverse group
        def rev(node, count, prev, nxt):
            if not node:
                return prev
            while count < k:
                nxt = node.next
                node.next = prev
                prev = node
                node = nxt
                count += 1
            return prev
        
        dummy = ListNode()
        out = dummy
        cur = head
        while head:
            for i in range(k - 1):
                if not head.next:
                    out.next = cur
                    return dummy.next
                head = head.next

            prev = head.next
            out.next = rev(cur, 0, prev, None)
            out = cur
            cur = cur.next
            head = cur


        return dummy.next  
        
