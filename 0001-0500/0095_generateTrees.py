# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.buildBST(1, n)

    def buildBST(self, l, r):
        trees = []
        for root in range(l, r + 1):
            for left in self.buildBST(l, root - 1):
                for right in self.buildBST(root + 1, r):
                    node = TreeNode(root)
                    node.left = left
                    node.right = right
                    trees.append(node)
        return trees or [None]

# Alternative solution

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        self.result = []
        
        for i in range(1, n + 1):
            root = TreeNode(i)
            nums = list(range(1, i)) + list(range(i + 1, n + 1))
            self.dfs(nums, root)

        listRepresentation = []

        for i, tree in enumerate(self.result):
            listRepresentation.append(self.convertBST(tree, i))

        listRepresentation.sort()

        duplicates = set()

        for i in range(1, len(listRepresentation)):
            tree, idx = listRepresentation[i]

            if tree == listRepresentation[i - 1][0]:
                duplicates.add(idx)

        self.result = [tree for i, tree in enumerate(self.result) if i not in duplicates]

        return self.result

    def convertBST(self, tree, idx):
        result = []
        queue = deque([tree])

        while queue:
            node = queue.popleft()

            if not node:
                result.append(0)
                continue

            result.append(node.val)
            queue.append(node.left if node.left else None)
            queue.append(node.right if node.right else None)
        
        return result, idx

    def dfs(self, nums, root):        
        if not nums:
            self.result.append(self.copyOfBST(root))
            return

        for i in range(len(nums)):
            self.insertIntoBST(root, nums[i])
            self.dfs(nums[:i] + nums[i + 1:], root)
            self.deleteFromBST(root, nums[i])
        
    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)

        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)

        return root

    def deleteFromBST(self, root, val):         
        if root.left and root.left.val == val:
            root.left = None
            return

        if root.right and root.right.val == val:
            root.right = None
            return

        if val < root.val:
            return self.deleteFromBST(root.left, val)
        else:
            return self.deleteFromBST(root.right, val)

    def copyOfBST(self, root):
        if not root:
            return

        node = TreeNode(root.val)
        node.left = self.copyOfBST(root.left)
        node.right = self.copyOfBST(root.right)

        return node
