# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        self.div_and_con(root, preorder[1:], postorder[:-1])
        return root

    def div_and_con(self, root, pre, post):
        if not pre:
            return root
        elif len(pre) == 1:
            root.left = TreeNode(pre[0])
            return root
        elif len(pre) == 2:
            if pre == post:
                root.left = TreeNode(pre[0])
                root.right = TreeNode(pre[1])
            else:
                root.left = TreeNode(pre[0])
                root.left.left = TreeNode(pre[1])
            return root
        if pre[0] == post[-1]:
            root.left = self.div_and_con(TreeNode(pre[0]), pre[1:], post[:-1])
        if pre[0] != post[-1]:
            idx = pre.index(post[-1])
            root.left = self.div_and_con(TreeNode(pre[0]), pre[1:idx], post[:idx-1])
            root.right = self.div_and_con(TreeNode(post[-1]), pre[idx+1:], post[idx:len(post)-1])
        return root
