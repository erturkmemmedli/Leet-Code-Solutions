# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.goodPairs = 0
        self.list = self.dfs(root, distance)
        return self.goodPairs

    def dfs(self, node, distance):
        if not node.left and not node.right:
            return [[0, 0]]
        elif not node.left:
            left = None
            right = self.dfs(node.right, distance)
        elif not node.right:
            left = self.dfs(node.left, distance)
            right = None
        else:
            left = self.dfs(node.left, distance)
            right = self.dfs(node.right, distance)
        if left == right == [0, 0]:
            if distance >= 2:
                self.goodPairs += 1
            return [[1, 1], [1, 1]]
        elif left is None:
            temp = []
            for a, b in right:
                if b:
                    temp.append([a+1, b])
                else:
                    temp.append([a+1, 1])
            return temp
        elif right is None:
            temp = []
            for a, b in left:
                if b:
                    temp.append([a+1, b])
                else:
                    temp.append([a+1, 1])
            return temp
        else:
            tempLeft = []
            if len(left) == 2 and left[0] == left[1]:
                tempLeft.append([left[0][0] + 1, left[0][1] * 2])
            else:
                for a, b in left:
                    if b:
                        tempLeft.append([a+1, b])
                    else:
                        tempLeft.append([a+1, 1])
            tempRight = []
            if len(right) == 2 and right[0] == right[1]:
                tempRight.append([right[0][0] + 1, right[0][1] * 2])
            else:
                for a, b in right:
                    if b:
                        tempRight.append([a+1, b])
                    else:
                        tempRight.append([a+1, 1])
            for x, y in tempLeft:
                for u, v in tempRight:
                    if x + u <= distance:
                        self.goodPairs += y * v
            return tempLeft + tempRight
          
# Alternatie solution
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.goodPairs = 0
        self.list = self.dfs(root, distance)
        return self.goodPairs

    def dfs(self, node, distance):
        if not node.left and not node.right:
            return [[0, 0]]
        elif not node.left:
            left = None
            right = self.dfs(node.right, distance)
        elif not node.right:
            left = self.dfs(node.left, distance)
            right = None
        else:
            left = self.dfs(node.left, distance)
            right = self.dfs(node.right, distance)
        if left == right == [0, 0]:
            if distance >= 2:
                self.goodPairs += 1
            return [[1, 1], [1, 1]]
        elif left is None:
            return self.helper(right, False)
        elif right is None:
            return self.helper(left, False)
        else:
            tempLeft = self.helper(left, True)
            tempRight = self.helper(right, True)
            for x, y in tempLeft:
                for u, v in tempRight:
                    if x + u <= distance:
                        self.goodPairs += y * v
            return tempLeft + tempRight
        
    def helper(self, arr, flag):
        if flag and len(arr) == 2 and arr[0] == arr[1]:
            temp = [[arr[0][0] + 1, arr[0][1] * 2]]
        else:
            temp = []
            for a, b in arr:
                if b:
                    temp.append([a+1, b])
                else:
                    temp.append([a+1, 1])
        return temp
