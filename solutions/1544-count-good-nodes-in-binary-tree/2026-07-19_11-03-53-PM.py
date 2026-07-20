# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.out = 0

        def dfs(node, val):
            if not node:
                return 
            if node.val >= val:
                self.out += 1
            dfs(node.left, max(val, node.val))
            dfs(node.right, max(val, node.val))

        dfs(root, root.val)
        return self.out
            
            
