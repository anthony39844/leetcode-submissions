# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def left(node, min_n, max_n):
            if not node:
                return True
            if node.val > min_n and node.val < max_n:
                return left(node.left, min_n, node.val) and right(node.right, node.val, max_n)
            return False

        def right(node, min_n, max_n):
            if not node:
                return True
            if node.val > min_n and node.val < max_n:
                return left(node.left, min_n, node.val) and right(node.right, node.val, max_n)
            return False
        
        return left(root.left, float('-inf'), root.val) and right(root.right, root.val, float('inf'))
