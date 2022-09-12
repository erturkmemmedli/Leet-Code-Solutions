# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict
from copy import copy

class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        pseudo_palindromic = []
        hashmap = defaultdict(int, {root.val : 1})
        self.dfs(root, pseudo_palindromic, hashmap)
        count = 0
        for path in pseudo_palindromic:
            odds = 0
            for val in path.values():
                if val % 2 == 1:
                    odds += 1
                if odds > 1:
                    break
            if odds <= 1:
                count += 1
        return count    
        
    def dfs(self, node, output, hashmap):
        if not node.left and not node.right:
            output.append(hashmap.copy())
            return
        if node.left:
            hashmap[node.left.val] += 1
            self.dfs(node.left, output, hashmap)
            hashmap[node.left.val] -= 1
        if node.right:
            hashmap[node.right.val] += 1
            self.dfs(node.right, output, hashmap)
            hashmap[node.right.val] -= 1
            
# Alternative solution

from collections import defaultdict

class Solution1:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.count = 0
        hashmap = defaultdict(int, {root.val : 1})
        self.dfs(root, hashmap)
        return self.count    
        
    def dfs(self, node, hashmap):
        if not node.left and not node.right:
            x = sum(val % 2 == 1 for val in hashmap.values())
            if x <= 1: self.count += 1
            return
        if node.left:
            hashmap[node.left.val] += 1
            self.dfs(node.left, hashmap)
            hashmap[node.left.val] -= 1
        if node.right:
            hashmap[node.right.val] += 1
            self.dfs(node.right, hashmap)
            hashmap[node.right.val] -= 1
