# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from sortedcontainers import SortedList

class Solution:
    def __init__(self):
        self.list = SortedList()
        
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        self.inorder(root1)
        self.inorder(root2)
        return self.list
        
    def inorder(self, node):
        if not node: return
        self.inorder(node.left)
        self.list.add(node.val)
        self.inorder(node.right)
        
# Alternative solution

class Solution1:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        list1, list2 = [], []
        self.inorder(root1, list1)
        self.inorder(root2, list2)
        new_list = []
        i = 0
        j = 0
        while i < len(list1) and j < len(list2):
            if list1[i] <= list2[j]:
                new_list.append(list1[i])
                i += 1
            else:
                new_list.append(list2[j])
                j += 1
        if j == len(list2):
            new_list += list1[i:]
        elif i == len(list1):
            new_list += list2[j:]
        return new_list
        
    def inorder(self, node, L):
        if not node: return
        self.inorder(node.left, L)
        L.append(node.val)
        self.inorder(node.right, L)
