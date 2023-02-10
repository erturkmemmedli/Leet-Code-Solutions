# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root: return 0
        self.path = []
        self.count = 0
        self.dfs(root, targetSum)
        return self.count

    def dfs(self, node, targetSum):
        if not node:
            return
        for i in range(len(self.path)):
            self.path[i] -= node.val
            if self.path[i] == 0: self.count += 1
        if targetSum - node.val == 0: self.count += 1
        self.path.append(targetSum - node.val)
        self.dfs(node.left, targetSum)
        self.dfs(node.right, targetSum)
        for i in range(len(self.path) - 1):
            self.path[i] += node.val
        self.path.pop()

# Alternative solution

class Solution1:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root: return 0
        self.result = 0
        self.dfs(root, targetSum, 0, collections.defaultdict(int, {0:1}))
        return self.result

    def dfs(self, node, targetSum, currentSum, memo):
        if not node: return
        currentSum += node.val
        previousSum = currentSum - targetSum
        self.result += memo[previousSum]
        memo[currentSum] += 1
        self.dfs(node.left, targetSum, currentSum, memo)
        self.dfs(node.right, targetSum, currentSum, memo)
        memo[currentSum] -= 1
        
# Alternative solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.total = 0
        self.dfs(root, targetSum)
        return self.total

    def dfs(self, node, target):
        if not node:
            return {}
        leftDict = self.dfs(node.left, target)
        rightDict = self.dfs(node.right, target)
        if node.val == target:
            self.total += 1
        newDict = {node.val: 1}
        for num in leftDict.keys():
            newNum = num + node.val
            newDict[newNum] = newDict.get(newNum, 0) + leftDict[num]
            if newNum == target:
                self.total += leftDict[num]
        for num in rightDict.keys():
            newNum = num + node.val
            newDict[newNum] = newDict.get(newNum, 0) + rightDict[num]
            if newNum == target:
                self.total += rightDict[num]
        return newDict
