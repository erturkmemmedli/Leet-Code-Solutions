# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class CBTInserter:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root

    def insert(self, val: int) -> int:
        Q = deque([[self.root]])
        while Q:
            level = Q.popleft()
            new_level = []
            for node in level:
                if node.left:
                    new_level.append(node.left)
                else:
                    node.left = TreeNode(val)
                    return node.val
                if node.right:
                    new_level.append(node.right)
                else:
                    node.right = TreeNode(val)
                    return node.val
            if new_level:
                Q.append(new_level)

    def get_root(self) -> Optional[TreeNode]:
        return self.root

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()

# Alternative solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class CBTInserter1:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.list = deque()
        self.bfs_tree_to_list()

    def insert(self, val: int) -> int:
        self.list.append(val)
        n = len(self.list) // 2
        return self.list[n-1]

    def get_root(self) -> Optional[TreeNode]:
        root = TreeNode(self.list.popleft())
        self.bfs_build_tree(root)
        return root
    
    def bfs_tree_to_list(self):
        Q = deque([[self.root]])
        while Q:
            level = Q.popleft()
            new_level = []
            for node in level:
                self.list.append(node.val)
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)
            if new_level:
                Q.append(new_level)
                
    def bfs_build_tree(self, root):
        Q = deque([root])
        while self.list:
            node = Q.popleft()
            node.left = TreeNode(self.list.popleft())
            Q.append(node.left)
            if self.list:
                node.right = TreeNode(self.list.popleft())
                Q.append(node.right)   

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()
