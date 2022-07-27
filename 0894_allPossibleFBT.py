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
