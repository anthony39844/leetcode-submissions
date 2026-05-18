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
            
            # choose the max value path 
            single_path = node.val + max(left, right, 0)

            # track the max path between having curr node as the root or being part of the path
            res = max(res, node.val + left + right, single_path)
            
            return single_path
        
        dfs(root)
        return res
