# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from bisect import bisect_left

class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """   
        self.string = ""
        self.preorder_traversal(root)
        return self.string
    
    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        preorder_list = []
        i = 0
        num = ""
        while i < len(data):
            if data[i] != "-":
                num += data[i]
            else:
                preorder_list.append(int(num))
                num = ""
            i += 1
        return self.binary_build(preorder_list)
        
    def preorder_traversal(self, node):
        if not node: return
        self.string += str(node.val) + "-"
        self.preorder_traversal(node.left)
        self.preorder_traversal(node.right)
        
    def binary_build(self, array):
        if not array: return
        val = array[0]
        index = bisect_left(array[1:], val)
        root = TreeNode(val)
        root.left = self.binary_build(array[1:index+1])
        root.right = self.binary_build(array[index+1:])
        return root

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans

# Alternative solution

from bisect import bisect_left

class Codec1:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """   
        self.string = ""
        self.preorder_traversal(root)
        return self.string
    
    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        preorder_list = [int(i) for i in data.split()]
        return self.binary_build(preorder_list)
        
    def preorder_traversal(self, node):
        if not node: return
        self.string += str(node.val) + " "
        self.preorder_traversal(node.left)
        self.preorder_traversal(node.right)
        
    def binary_build(self, array):
        if not array: return
        val = array[0]
        index = bisect_left(array[1:], val)
        root = TreeNode(val)
        root.left = self.binary_build(array[1:index+1])
        root.right = self.binary_build(array[index+1:])
        return root
