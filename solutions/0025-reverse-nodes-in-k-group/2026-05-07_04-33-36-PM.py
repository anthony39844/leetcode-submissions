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
            # head moves per group
            for i in range(k - 1):
                # group isnt long enough, append the remaining list
                if not head.next:
                    out.next = cur
                    return dummy.next
                head = head.next

            # set prev to be the start of the next group
            prev = head.next
            out.next = rev(cur, 0, prev, None)
            # move out up to the end of the reversed group
            # cur was originally the beginning of the group, after rev() its now the end
            out = cur
            cur = cur.next
            head = cur


        return dummy.next  
        
