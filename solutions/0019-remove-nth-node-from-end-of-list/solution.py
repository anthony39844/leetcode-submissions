# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        time = o(n)
        space = o(1)
        '''
        fast = head
        slow = head

        for i in range(n):
            fast = fast.next
        
        while fast and fast.next:
            fast = fast.next
            slow = slow.next

        if not fast:
            if slow == head:
                if slow.next:
                    return slow.next
                return None
                
        if slow.next.next:
            slow.next = slow.next.next
        else:
            slow.next = None

        return head

