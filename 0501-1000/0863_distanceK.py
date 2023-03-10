# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.array = []
        self.parent = {}
        self.assign_parents(root, k, None)
        self.solution(target, k, set([target.val]))
        return self.array
        
    def assign_parents(self, root, k, parent):
        if not root:
            return
        self.parent[root.val] = parent
        if not root.left and not root.right:
            return
        self.assign_parents(root.left, k, root)
        self.assign_parents(root.right, k, root)

    def solution(self, node, k, visited):
        if k == 0:
            self.array.append(node.val)
            return
        if self.parent[node.val] and self.parent[node.val].val not in visited:
            visited.add(self.parent[node.val].val)
            self.solution(self.parent[node.val], k - 1, visited)
            visited.remove(self.parent[node.val].val)
        if node.left and node.left.val not in visited:
            visited.add(node.left.val)
            self.solution(node.left, k - 1, visited)
            visited.remove(node.left.val)
        if node.right and node.right.val not in visited:
            visited.add(node.right.val)
            self.solution(node.right, k - 1, visited)
            visited.remove(node.right.val)
