# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.out = 0
        def count(node):
            if not node:
                return 0
            x = count(node.left) 
            y = count(node.right)
            self.out = max(self.out, x + y)
            return 1 + max(x, y)

        count(root)
        return self.out
