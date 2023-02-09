# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        nodeToDelete, parent = self.binarySearch(root, None, key)
        if nodeToDelete is None:
            return root
        if not nodeToDelete.left and not nodeToDelete.right:
            if not parent:
                return None
            else:
                if nodeToDelete == parent.left:
                    parent.left = None
                if nodeToDelete == parent.right:
                    parent.right = None
            return root
        elif not nodeToDelete.left:
            if not parent:
                return root.right
            else:
                if nodeToDelete == parent.left:
                    parent.left = nodeToDelete.right
                if nodeToDelete == parent.right:
                    parent.right = nodeToDelete.right
            return root
        elif not nodeToDelete.right:
            if not parent:
                return root.left
            else:
                if nodeToDelete == parent.left:
                    parent.left = nodeToDelete.left
                if nodeToDelete == parent.right:
                    parent.right = nodeToDelete.left
            return root
        else:
            nodeToReplace, father = self.rightDescendant(nodeToDelete.right, nodeToDelete)
            if not parent:
                if nodeToReplace == nodeToDelete.right:
                    nodeToReplace.left = nodeToDelete.left
                    return nodeToReplace
                else:
                    father.left = nodeToReplace.right
                    nodeToReplace.left = nodeToDelete.left
                    nodeToReplace.right = nodeToDelete.right
                    return nodeToReplace
            else:
                if nodeToReplace == nodeToDelete.right:
                    nodeToReplace.left = nodeToDelete.left
                    if nodeToDelete == parent.left:
                        parent.left = nodeToReplace
                    if nodeToDelete == parent.right:
                        parent.right = nodeToReplace
                    return root
                else:
                    father.left = nodeToReplace.right
                    nodeToReplace.left = nodeToDelete.left
                    nodeToReplace.right = nodeToDelete.right
                    if nodeToDelete == parent.left:
                        parent.left = nodeToReplace
                    if nodeToDelete == parent.right:
                        parent.right = nodeToReplace
                    return root

    def binarySearch(self, node, parent, key):
        if not node:
            return node, parent
        if key > node.val:
            return self.binarySearch(node.right, node, key)
        elif key < node.val:
            return self.binarySearch(node.left, node, key)
        else:
            return node, parent

    def rightDescendant(self, node, parent):
        if node.left:
            return self.rightDescendant(node.left, node)
        return node, parent

# Alternative solution

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                node = root.right
                while node.left:
                    node = node.left
                root.val = node.val
                root.right = self.deleteNode(root.right, root.val)
        return root
