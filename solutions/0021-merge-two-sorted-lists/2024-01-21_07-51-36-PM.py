# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        if not list1:
            return list2
        if not list2: 
            return list1
        if list1.val <= list2.val:
            curr = list1
            head = curr
            curr1 = curr1.next
        else:
            curr = list2
            head = curr
            curr2 = curr2.next
        while curr1 and curr2:
            if curr1.val >= curr2.val:
               curr.next = curr2
               curr2 = curr2.next
            else:
                curr.next = curr1
                curr1 = curr1.next
            curr = curr.next
        while curr1:
            curr.next = curr1
            curr1 = curr1.next
            curr = curr.next
        while curr2:
            curr.next = curr2
            curr2 = curr2.next
            curr = curr.next

        return head
        

