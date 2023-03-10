class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        tree = [(1,1)]
        inverse = True
        last = 1
        while last < label:
            new_last = 2 * last + 1
            if inverse:
                tree.append((new_last, last+1))
                inverse = False
            else:
                tree.append((last+1, new_last))
                inverse = True
            last = new_last
        path = []
        if tree[-1][0] > tree[-1][1]:
            index = tree[-1][0] - label
        else:
            index = label - tree[-1][0]

        for i in range(len(tree)-1, -1, -1):
            if tree[i][0] > tree[i][1]:
                path.append(tree[i][0] - index)
            else:
                path.append(tree[i][0] + index)
            index //= 2
        return path[::-1]
