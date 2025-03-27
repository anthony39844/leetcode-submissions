# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def search(node):
            if not node:
                return 0
            maxL = search(node.left) + 1
            maxR = search(node.right) + 1

            return max(maxL, maxR)

        return search(root)
