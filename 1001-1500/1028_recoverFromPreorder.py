# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        k = 0
        for i in range(len(traversal)):
            if traversal[i] != "-":
                k += 1
            else:
                break
        level = deque([deque([[int(traversal[:k])]]), deque([[]])])
        depth = 0
        num_string = ""
        for i in range(k, len(traversal)):
            if traversal[i] == '-':
                depth += 1
            else:
                if i + 1 < len(traversal) and traversal[i + 1] != "-":
                    num_string += traversal[i]
                    continue
                else:
                    num_string += traversal[i]
                    if depth == len(level) - 1:
                        level[depth][-1].append(int(num_string))
                        level.append(deque([[]]))
                    else:
                        level[depth][-1].append(int(num_string))
                        level[depth + 1].append([])
                    depth = 0
                    num_string = ""
        return self.bfs(level)

    def bfs(self, level):
        root = TreeNode(level.popleft()[0][0])
        queue = deque([root])
        while len(level) > 1:
            if not level[0]:
                level.popleft()
                continue
            pair = level[0].popleft()
            node = queue.popleft()
            if not pair:
                continue
            if len(pair) >= 1:
                left = TreeNode(pair[0])
                node.left = left
                queue.append(left)
            if len(pair) == 2:
                right = TreeNode(pair[1])
                node.right = right
                queue.append(right)
        return root

# The question has been prepared based on the following class:
# build = PreorderTraversalString()
# build.dfs(node, depth = 0)
# Where node is root of the tree.

class PreorderTraversalString:
    def __init__(self):
        self.string = ""
        
    def dfs(self, node, depth):
        if not node: return
        self.string += "-" * depth +  str(node.val)
        print(self.string)
        self.dfs(node.left, depth + 1)
        self.dfs(node.right, depth + 1)
    
    def show(self):
        return self.string

# Alternative solution

class Solution1:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = []
        i = 0
        while i < len(traversal):
            level = 0
            value = ""
            while i < len(traversal) and traversal[i] == '-':
                level += 1
                i += 1
            while i < len(traversal) and traversal[i] != "-":
                value += traversal[i]
                i += 1
            node = TreeNode(int(value))
            while len(stack) > level:
                stack.pop()
            if stack and stack[-1].left is None:
                stack[-1].left = node
            elif stack:
                stack[-1].right = node
            stack.append(node)
        return stack[0]

# Alternative solution

class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        hashmap = defaultdict(list)
        val = ""
        depth = 0

        def build_tree(val, depth):
            val = int(val)
            node = TreeNode(val)
            hashmap[depth].append(node)
            if depth - 1 in hashmap:
                if not hashmap[depth - 1][-1].left:
                    hashmap[depth - 1][-1].left = node
                else:
                    hashmap[depth - 1][-1].right = node
        
        for i, char in enumerate(traversal):
            if char != '-':
                val += char
                if i == len(traversal) - 1:
                    build_tree(val, depth)
            else:
                if val:
                    build_tree(val, depth)
                    val = ""
                    depth = 0
                depth += 1

        return hashmap[0][0]
