# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.list = []
        self.inorder(root)       
        self.i = 0

    def next(self) -> int:
        self.i += 1
        return self.list[self.i - 1]

    def hasNext(self) -> bool:
        return self.i < len(self.list)
        
    def inorder(self, node):
        if not node: return
        self.inorder(node.left)
        self.list.append(node.val)
        self.inorder(node.right)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
