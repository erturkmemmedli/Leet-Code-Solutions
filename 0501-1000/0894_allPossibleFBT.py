# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.storage = {0: [], 1: {TreeNode()}}
        
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n not in self.storage:
            temp = []
            for x in range(n):
                for left in self.allPossibleFBT(x):
                    for right in self.allPossibleFBT(n-1-x):
                        root = TreeNode()
                        root.left = left
                        root.right = right
                        temp.append(root)
            self.storage[n] = temp
        return self.storage[n]

# Alternative solution

class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        self.memo = {0 : [], 1 : [TreeNode()]}
        self.dp(n)
        return self.memo[n]

    def dp(self, n):
        if n in self.memo:
            return self.memo[n]

        trees = []
        
        for i in range(n):
            for leftNode in self.dp(i):
                for rightNode in self.dp(n - i - 1):
                    root = TreeNode()
                    root.left = leftNode
                    root.right = rightNode
                    trees.append(root)

        self.memo[n] = trees[:]
        return self.memo[n]
