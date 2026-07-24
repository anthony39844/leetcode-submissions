# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.out = -1
        self.count = 0

        def dfs(node):
            if not node or self.out > -1:
                return 
            
            dfs(node.left)
            self.count += 1
            if self.count == k:
                self.out = node.val
                return
            dfs(node.right)
        
        dfs(root)
        return self.out


# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         stack = []
#         curr = root
        
#         while stack or curr:
#             # Go as far left as possible
#             while curr:
#                 stack.append(curr)
#                 curr = curr.left
            
#             # Process the node
#             curr = stack.pop()
#             k -= 1
#             if k == 0:
#                 return curr.val
            
#             # Move to the right
#             curr = curr.right
