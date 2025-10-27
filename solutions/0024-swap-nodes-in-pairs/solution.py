# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        time = o(n)
        space = o(1)
        '''
        if not head:
            return None
        if not head.next and head: 
            return head
            
        dummy = ListNode(0, head)
        prev = dummy
        first = head 
        second = first.next 

        while second: 
            prev.next = second 
            first.next = second.next 
            second.next = first 

            prev = first 
            first = first.next 
            if first: 
                # odd length list, or more swaps needed
                second = first.next
            else:
                break

        return dummy.next
