# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if not node:
                return 0

            x = dfs(node.left)

            # pruning
            if x == -1: return -1
            y = dfs(node.right)
            if y == -1: return -1

            if abs(x - y) > 1:
                return -1

            return 1 + max(x, y)

        return dfs(root) != -1
