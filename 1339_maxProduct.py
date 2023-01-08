# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        total = self.constructSumPointers(root)
        self.maxSplitProduct = 0
        self.maxSplitProductCalculation(root, total)
        return self.maxSplitProduct % 1_000_000_007

    def constructSumPointers(self, node):
        if not node: return 0
        node.leftSum, node.rightSum = self.constructSumPointers(node.left), self.constructSumPointers(node.right)
        node.sum = node.leftSum + node.rightSum + node.val
        return node.sum

    def maxSplitProductCalculation(self, node, total):
        if not node: return
        self.maxSplitProduct = max(self.maxSplitProduct, (total - node.sum) * node.sum)
        self.maxSplitProductCalculation(node.left, total)
        self.maxSplitProductCalculation(node.right, total)
