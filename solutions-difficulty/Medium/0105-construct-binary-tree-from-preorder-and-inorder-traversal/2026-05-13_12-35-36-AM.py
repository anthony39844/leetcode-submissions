# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.i = 0

        idx = {val: i for i, val in enumerate(inorder)}

        def build(l, r):
            if l > r:
                return 
            
            m = idx[preorder[self.i]]
            root = TreeNode(inorder[m])
            self.i += 1
            root.left = build(l, m - 1)
            root.right = build(m + 1, r)
            return root

        return build(0, len(preorder) - 1)

      
