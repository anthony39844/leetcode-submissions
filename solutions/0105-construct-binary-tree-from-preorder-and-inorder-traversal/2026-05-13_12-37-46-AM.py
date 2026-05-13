# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        i = 0

        idx = {val: i for i, val in enumerate(inorder)}

        def build(l, r):
            if l > r:
                return 
            nonlocal i
            
            # the root node
            m = idx[preorder[i]]
            root = TreeNode(inorder[m])

            # move to next node in preorder (root node of subtree)
            i += 1

            # build tree recursively
            # send in the left subtree of current root
            root.left = build(l, m - 1)

            # right subtree of current root
            root.right = build(m + 1, r)
            return root

        return build(0, len(preorder) - 1)

      
