# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        # root of a subtree
        root = TreeNode(val=preorder[0])

        # if are at the only node in a subtree
        if len(preorder) == 1:
            return root
        
        # index of root in the inorder arr, used to find the left and right subtrees of this root node
        m = inorder.index(preorder[0])

        # build the subtree recursively
        # 1:m+1 => node after current root node to the end of the left subtree in preorder arr
        # 0:m => left subtree in inorder arr
        root.left = self.buildTree(preorder[1:m+1], inorder[0:m])

        # m+1: => right subtree in preorder arr
        # m+1: => right subtree in inorder arr
        root.right = self.buildTree(preorder[m+1:], inorder[m+1:])

        # return the subtree
        return root

      
