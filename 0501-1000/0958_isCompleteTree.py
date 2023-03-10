# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        Queue = collections.deque([root])
        levelNodeCount = 1
        notEnoughNodeFlag = False
        while Queue:
            for _ in range(len(Queue)):
                node = Queue.popleft()
                if notEnoughNodeFlag and (node.left or node.right):
                    return False
                if not node.left and node.right:
                    return False
                if not node.left or not node.right:
                    notEnoughNodeFlag = True
                if node.left:
                    Queue.append(node.left)
                if node.right:
                    Queue.append(node.right)
            if len(Queue) < 2 * levelNodeCount:
                 notEnoughNodeFlag = True
            levelNodeCount *= 2
        return True
