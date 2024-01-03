# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        depth_map = defaultdict(int)
        height_map = defaultdict(int)
        cousins = defaultdict(list)

        self.calculate_height(root, depth_map, height_map, 0)

        for root_val, depth in depth_map.items():
            cousins[depth].append((-height_map[root_val], root_val))
            cousins[depth].sort()

            if len(cousins[depth]) > 2:
                cousins[depth].pop()

        output = []

        for query in queries:
            depth = depth_map[query]

            if len(cousins[depth]) == 1:
                output.append(depth - 1)
            elif cousins[depth][0][1] == query:
                output.append(-cousins[depth][1][0] + depth)
            else:
                output.append(-cousins[depth][0][0] + depth)

        return output

    def calculate_height(self, root, depth_map, height_map, depth):
        if not root:
            return -1

        depth_map[root.val] = depth

        left = self.calculate_height(root.left, depth_map, height_map, depth + 1)
        right = self.calculate_height(root.right, depth_map, height_map, depth + 1)
        height = max(left, right) + 1

        height_map[root.val] = height

        return height
