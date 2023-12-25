# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def canMerge(self, trees: List[TreeNode]) -> Optional[TreeNode]:
        tree_map = {}
        self.nodes = set()
        excludes = set()

        for root in trees:
            tree_map[root.val] = root
            self.nodes.add(root.val)
            excludes.add(root.val)

            if root.left:
                self.nodes.add(root.left.val)
            if root.right:
                self.nodes.add(root.right.val)

        for tree in tree_map.values():
            if tree.left and tree.left.val in tree_map:
                excludes.discard(tree.left.val)
                tree.left = tree_map[tree.left.val]
            if tree.right and tree.right.val in tree_map:
                excludes.discard(tree.right.val)
                tree.right = tree_map[tree.right.val]

        if len(excludes) != 1:
            return None

        root = tree_map[excludes.pop()]
        return root if self.is_bst(root, -float('inf'), float('inf')) and not self.nodes else None

    def is_bst(self, root, mnm, mxm):
        if not root:
            return True
        
        if root.val not in self.nodes:
            return False
        
        self.nodes.remove(root.val)
        
        left = self.is_bst(root.left, mnm, root.val)
        right = self.is_bst(root.right, root.val, mxm)
        
        if left and (root.val < mnm or root.val > mxm):
            return False
            
        if right and (root.val < mnm or root.val > mxm):
            return False

        return left and right
