# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root: return ""
        tree = str(root.val)
        queue = collections.deque([root])
        nulls = ""
        while queue:
            node = queue.popleft()
            if node.left and node.right:
                if nulls:
                    tree += nulls
                    nulls = ""
                tree += "," + str(node.left.val) + "," + str(node.right.val)
                queue.append(node.left)
                queue.append(node.right)
            elif node.left and not node.right:
                if nulls:
                    tree += nulls
                    nulls = ""
                tree += "," + str(node.left.val) + "," + "null"
                queue.append(node.left)
            elif not node.left and node.right:
                if nulls:
                    tree += nulls
                    nulls = ""
                tree += "," + "null" + "," + str(node.right.val)
                queue.append(node.right)
            else:
                nulls += "," + "null" + "," + "null"
        return tree

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if not data: return
        tree = data.split(",")
        root = TreeNode(int(tree[0]))
        queue = collections.deque([[root]])
        index = 1
        while queue and index < len(tree):
            level = queue.popleft()
            newLevel = []
            for node in level:
                if index >= len(tree):
                    break
                if tree[index] != "null":
                    left = TreeNode(int(tree[index]))
                    node.left = left
                    newLevel.append(left)
                index += 1
                if tree[index] != "null":
                    right = TreeNode(int(tree[index]))
                    node.right = right
                    newLevel.append(right)
                index += 1
            if newLevel:
                queue.append(newLevel)
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
