# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head #the latter half of the list
        fast = head
        count = 0
            
        while fast.next:
            fast = fast.next
            if count % 2 == 0:
                slow = slow.next
            count += 1

        current = slow #this is reversing the latter half of the list
        rev = None
        while current:
            next_node = current.next
            current.next = rev
            rev = current
            current = next_node
        """
        curr = head 
        print(rev)
        next = curr.next #nodes after
        print(next)
        curr.next = rev #set next node to rev
        print(curr)
        curr = curr.next #move curr up
        print(curr)
        rev = rev.next #move rev up 
        print(rev)
        curr.next = next #set next to the next 
        print(curr)
        print(head)
        next = next.next #move next up
        print(next)
        curr = curr.next #move curr up again
        print(curr)
        curr.next = rev #set next to the next rev
        """
        curr = head
        next = curr.next
        while rev.next:
            curr.next = rev
            curr = curr.next
            rev = rev.next
            curr.next = next
            next = next.next
            curr = curr.next


            
        
        



        

