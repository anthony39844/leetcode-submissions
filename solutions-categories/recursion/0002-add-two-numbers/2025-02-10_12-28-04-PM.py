# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        cur = dummy

        while l1 and l2:
            x = l1.val + l2.val
            if carry:
                x += 1
                carry = 0
            if x >= 10:
                carry = 1
                x -= 10
            cur.next = ListNode(x)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            x = l1.val
            if carry:
                x += 1
                carry = 0
            if x >= 10:
                carry = 1
                x -= 10
            cur.next = ListNode(x)
            cur = cur.next
            l1 = l1.next
        
        while l2:
            x = l2.val
            if carry:
                x += 1
                carry = 0
            if x >= 10:
                carry = 1
                x -= 10
            cur.next = ListNode(x)
            cur = cur.next
            l2 = l2.next
        
        if carry:
            cur.next = ListNode(1)
        
        return dummy.next

