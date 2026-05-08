# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        # push each head of the list to the min heap, use i as a tiebreaker
        for i, x in enumerate(lists):
            if x:
                heapq.heappush(heap, (x.val, i, x))
        
        dummy = ListNode()
        cur = dummy

        while heap:
            x, i, node = heapq.heappop(heap)
            # if the node has a next, add that node to the heap (continuation of the linked list)
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
            node.next = None
            cur.next = node
            cur = cur.next

        return dummy.next
