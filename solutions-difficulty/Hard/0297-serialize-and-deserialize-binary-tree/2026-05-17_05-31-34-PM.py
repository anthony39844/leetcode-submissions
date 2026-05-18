# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        arr = []

        def dfs(node):
            nonlocal arr
            if not node: 
                arr.append("NONE")
                return

            arr.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(arr)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        # 1. Split the data and turn it into an iterator
        tokens = data.split(",")
        token_iter = iter(tokens)
        
        def build():
            x = next(token_iter)            
            
            if x == "NONE":
                return None            
            
            node = TreeNode(x)            
            
            node.left = build()
            node.right = build()

            return node            
            
        return build()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
