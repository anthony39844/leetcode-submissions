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
        s = [root]

        while s:
            x = s.pop()
            if x:
                arr.append(str(x.val))

                # append right first so LIFO can make left path is popped first
                s.append(x.right)
                s.append(x.left)
            else:
                arr.append("#")

        return ",".join(arr)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        # use an iterator so we dont track indexes
        tokens = data.split(",")
        token_iter = iter(tokens)
        
        def build():
            x = next(token_iter)            
            if x == "#":
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
