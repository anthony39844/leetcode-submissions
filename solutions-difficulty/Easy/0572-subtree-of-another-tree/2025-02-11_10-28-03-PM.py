# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if root == subRoot:
            return True

        def same(n1, n2):
            if not n1 and not n2:
                return True
            if (not n1 and n2) or (n1 and not n2):
                return False
            if n1.val != n2.val:
                return False
        
            return same(n1.left, n2.left) and same(n1.right, n2.right)
        

        def dfs(node, sub):
            if not node:
                return False
            else:
                if same(node, sub):
                    return True
                
            return dfs(node.left, sub) or dfs(node.right, sub)
        
        return dfs(root, subRoot)
                

