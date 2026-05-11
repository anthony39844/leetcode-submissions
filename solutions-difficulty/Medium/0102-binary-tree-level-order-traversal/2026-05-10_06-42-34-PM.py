# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        out = []
        q = deque([[root]])

        while q:
            nodes = q.popleft()
            arr = []
            level = []
            for node in nodes:
                if node:
                    level.append(node.val)
                    if node.left:
                        arr.append(node.left)
                    if node.right:
                        arr.append(node.right)
            if arr:
                q.append(arr)
            if level:
                out.append(level)
        
        return out
                
