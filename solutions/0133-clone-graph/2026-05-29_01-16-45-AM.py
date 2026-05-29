"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        visited = {}
        def dfs(node):
            if node in visited:
                return visited[node]
            
            x = Node(node.val)
            visited[node] = x
            for i in node.neighbors:
                x.neighbors.append(dfs(i))
            
            return x
 
        return dfs(node)
