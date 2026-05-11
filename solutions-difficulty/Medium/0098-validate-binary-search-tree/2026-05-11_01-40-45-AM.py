# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(node, min_n, max_n):
            if not node:
                return True
            if node.val > min_n and node.val < max_n:
                return validate(node.left, min_n, node.val) and validate(node.right, node.val, max_n)
            return False
        
        return validate(root, float('-inf'), float('inf'))
