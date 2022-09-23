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

# Alternative solution

from collections import deque
from bisect import bisect_left

class Codec2:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """   
        self.string = ""
        self.preorder_traversal(root)
        return self.string
    
    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        preorder_queue = deque(map(int, data.split()))
        return self.binary_build(preorder_queue, -float('inf'), float(inf))
        
    def preorder_traversal(self, node):
        if not node: return
        self.string += str(node.val) + " "
        self.preorder_traversal(node.left)
        self.preorder_traversal(node.right)
        
    def binary_build(self, queue, minimum, maximum):
        if not queue: return
        if minimum < queue[0] < maximum:
            val = queue.popleft()
            root = TreeNode(val)
            root.left = self.binary_build(queue, minimum, val)
            root.right = self.binary_build(queue, val, maximum)
            return root

# Alternative solution

from collections import deque

class Codec3:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """   
        if not root: return ""
        string = []
        bfs_queue = deque([root])
        while bfs_queue:
            node = bfs_queue.popleft()
            if node:
                string.append(str(node.val))
                bfs_queue.extend([node.left, node.right])
            else:
                string.append("*")
        return ' '.join(string)
    
    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data: return
        levelorder = deque(data.split())
        root_node = levelorder.popleft()
        root = TreeNode(int(root_node))
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if levelorder[0] != "*":
                left = levelorder.popleft()
                node.left = TreeNode(int(left))
                queue.append(node.left)
            else:
                levelorder.popleft()
            if levelorder[0] != "*":
                right = levelorder.popleft()
                node.right = TreeNode(int(right))
                queue.append(node.right)
            else:
                levelorder.popleft()
        return root