# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        fast = head.next
        slow = head
        count = 0
        while fast.next:
            fast = fast.next
            if count % 2 == 0:
                slow = slow.next
            count += 1
            if slow.val == fast.val:
                if slow.next == fast.next:
                    return True

        return False
