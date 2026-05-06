"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None
            
        d = {}
        cur = head
        while cur:
            d[cur] = Node(cur.val, cur.next, cur.random)
            cur = cur.next
        
        cur = head
        while cur:
            node = d[cur]
            node.next = d[node.next] if node.next in d else None
            node.random = d[node.random] if node.random in d else None
            cur = cur.next
        
        return d[head]

     

