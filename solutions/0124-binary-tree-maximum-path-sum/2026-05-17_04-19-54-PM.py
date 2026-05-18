# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def dfs(node):
            nonlocal res
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            single_path = node.val +max(left, right, 0)
            split_path = left + right + node.val
            res = max(res, single_path, split_path)
            
            return single_path
        
        dfs(root)
        return res
