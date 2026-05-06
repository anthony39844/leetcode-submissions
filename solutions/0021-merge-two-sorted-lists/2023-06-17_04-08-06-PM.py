# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1) #make dummy node
        current = dummy

        while list1 and list2: #while both lists are not empty
            if list1.val < list2.val: #point to list1 if list1 is less than
               current.next = list1
               list1 = list1.next #move list1 to the next node
            else: 
                current.next = list2 #point to list2 if list2 is less than
                list2 = list2.next #move list2 to the next node
            
            current = current.next #move current node to the next node
        
        if list1 or list2:
            current.next = list1 if list1 else list2
        
        return dummy.next

             
            
