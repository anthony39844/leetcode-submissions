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
        first = head 
        second = first.next 

        while second: 
            if prev: # not the first swap
                prev.next = second 
                first.next = second.next 
                second.next = first 
            else:
                first.next = second.next 
                second.next = first 
                head = second # make this the new head since we swapped
            prev = first 
            first = first.next 
            if first: 
                # odd length list, or more swaps needed
                second = first.next
            else:
                break

        return head
