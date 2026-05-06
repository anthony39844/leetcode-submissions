# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next and n == 1: 
            return None

        current = head #reverse list
        rev = None
        while current:
            next_node = current.next
            current.next = rev
            rev = current
            current = next_node #rev will be the head of the reversed list

        head2 = rev
        curr = rev

        for i in range(n - 1):
            curr = curr.next #loop to the correct node

        if n == 1:  #if n is 1 or we are removing the first node of the reversed list just move up rev
            rev = rev.next
            head2 = rev
        else: 
            for i in range(n - 2): #move rev to the node before the one we are moving
                rev = rev.next
            next = curr.next #else we get the node after the one we are removing 
            rev.next = next #and set the node after rev to next

        current = head2 #reverse the list back
        prev = None
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

