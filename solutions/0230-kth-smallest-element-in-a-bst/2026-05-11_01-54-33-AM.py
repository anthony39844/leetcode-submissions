# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        x = k

        def dfs(node):
            if not node:
                return None

            nonlocal x
            n = dfs(node.left)
            if n != None: return n

            x -= 1
            if x == 0:
                return node.val

            n = dfs(node.right)
            if n != None: return n
        
        return dfs(root)



