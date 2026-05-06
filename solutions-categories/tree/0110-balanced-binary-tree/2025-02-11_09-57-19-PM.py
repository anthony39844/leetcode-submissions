# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.out = True
        def depth(node):
            if not node:
                return 0
            else:
                l = depth(node.left)
                r = depth(node.right)
                if abs(l - r) > 1:
                    self.out = False
                return max(l, r) + 1
        depth(root)
        return self.out
