# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        root.val = 0
        self.root = self.dfs(root)

    def find(self, target: int) -> bool:
        nodes = [target]
        x = target
        while x:
            x = (x - 1) // 2
            nodes.append(x)
        nodes.reverse()
        temp = self.root
        for i in range(len(nodes)-1):
            if nodes[i+1] == 2 * nodes[i] + 1:
                if temp.left:
                    temp = temp.left
                else:
                    return False
            else:
                if temp.right:
                    temp = temp.right
                else:
                    return False
        return temp.val == target
        
    def dfs(self, node):
        if not node:
            return
        if node.left:
            node.left.val = 2 * node.val + 1
            self.dfs(node.left)
        if node.right:
            node.right.val = 2 * node.val + 2
            self.dfs(node.right)
        return node
        
# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
