# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def depth(node, count):
            if not node:
                return count
            return max(depth(node.left, count + 1), depth(node.right, count + 1))
        
        return depth(root, 0)
