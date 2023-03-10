# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.buildBST(1, n)

    def buildBST(self, l, r):
        trees = []
        for root in range(l, r + 1):
            for left in self.buildBST(l, root - 1):
                for right in self.buildBST(root + 1, r):
                    node = TreeNode(root)
                    node.left = left
                    node.right = right
                    trees.append(node)
        return trees or [None]
