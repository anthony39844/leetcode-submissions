# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def search(tree):
            

            def same(node1, node2):
                if not node1 and not node2:
                    return True
                elif (not node1 and node2) or (node1 and not node2):
                    return False
                if node1.val != node2.val:
                    return False
                
                return same(node1.left, node2.left) and same(node1.right, node2.right)
        
            if not tree:
                return False
            if same(tree, subRoot):
                return True
            return search(tree.left) or search(tree.right)
        
        return search(root)
            
