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

# Alternative solution

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        queue = deque([root])
        tree = ""

        while queue:
            size = len(queue)
            have_non_null = False

            for i in range(size):
                node = queue.popleft()
                if node == None:
                    tree += "*" if not tree else "#*"
                else:
                    tree += str(node.val) if not tree else "#" + str(node.val)
                    if node.left:
                        queue.append(node.left)
                        have_non_null = True
                    elif not node.left:
                        queue.append(None)
                    if node.right:
                        queue.append(node.right)
                        have_non_null = True
                    elif not node.right:
                        queue.append(None)
                    
            if not have_non_null:
                break

        return tree

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '*':
            return

        data = data.split('#')
        root = TreeNode(int(data[0]))
        queue = deque([root])
        idx = 1

        while queue:
            node = queue.popleft()
            if idx < len(data) and data[idx] != '*':
                node.left = TreeNode(int(data[idx]))
                queue.append(node.left)
            if idx + 1 < len(data) and data[idx + 1] != '*':
                node.right = TreeNode(int(data[idx + 1]))
                queue.append(node.right)
            idx += 2

        return root
