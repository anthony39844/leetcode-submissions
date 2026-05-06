# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: # no list
            return None
        if not head.next and head: # only one element
            return head

        prev = None # tracks previous node 
        first = head # tracks first one in pair
        second = first.next # track second one in pair

        while first.next:
            if prev:
                prev.next = second
                first.next = second.next
                second.next = first
            else:
                first.next = second.next
                second.next = first
                head = second
            prev = first
            first = first.next
            if first:
                second = first.next
            else:
                break

        return head
