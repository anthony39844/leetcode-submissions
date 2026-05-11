# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque([root]) 
        out = []

        while q:
            x = len(q)
            for i in range(x):
                node = q.popleft()
                if node:
                    # append them always from left to right, so the last node in the layer
                    # will be the one visible from the right
                    if i == x - 1:
                        out.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
        
        return out



