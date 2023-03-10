# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.nodes = []

    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        if not root or not voyage:
            return
        if root.val == voyage[0]:
            left, right = None, None
            if root.left:
                try:
                    left = voyage.index(root.left.val)
                except:
                    self.nodes = [-1]
                    return
            if root.right:
                try:
                    right = voyage.index(root.right.val)
                except:
                    self.nodes = [-1]
                    return
            if left and right:
                if left < right:
                    self.flipMatchVoyage(root.left, voyage[left:right])
                    self.flipMatchVoyage(root.right, voyage[right:])
                else:
                    self.nodes.append(root.val)
                    self.flipMatchVoyage(root.left, voyage[left:])
                    self.flipMatchVoyage(root.right, voyage[right:left])
            elif left and not right:
                self.flipMatchVoyage(root.left, voyage[1:])
            elif right and not left:
                self.flipMatchVoyage(root.right, voyage[1:])
        else:
            self.nodes = [-1]
        return self.nodes if -1 not in self.nodes else [-1]
