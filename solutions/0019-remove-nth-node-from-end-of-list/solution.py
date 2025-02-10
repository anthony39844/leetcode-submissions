# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        cur = head

        for i in range(n): #move up n spots
            cur = cur.next

        prev = dummy
        while cur: #move both up until cur is at the end, this will leave prev at 1 spot before the nth node from the end
            prev = prev.next
            cur = cur.next
        
        prev.next = prev.next.next 
        # node past nth node from end: will set it to that node
        # no past nth node from end: will set to None
        # removed only node list: prev will still be dummy so next.next will go to None so dummy.next will be None
        return dummy.next

