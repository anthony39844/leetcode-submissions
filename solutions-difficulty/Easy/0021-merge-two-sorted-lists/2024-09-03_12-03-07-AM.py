# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None
        if list1 == None:
            return list2
        if list2 == None:
            return list1

        merged = ListNode()
        cur1 = list1
        cur2 = list2
        if cur1.val < cur2.val:
            merged = list1
            cur1 = cur1.next
        else:
            merged = list2
            cur2 = cur2.next
        merge_head = merged
        while cur1 and cur2:
            print(merge_head)
            print(cur1)
            print(cur2)
            if cur1.val < cur2.val:
                merged.next = cur1
                cur1 = cur1.next
            else:
                merged.next = cur2
                cur2 = cur2.next
            merged = merged.next
        
        if cur1:
            merged.next = cur1

        if cur2:
            merged.next = cur2

        return merge_head
        

                
