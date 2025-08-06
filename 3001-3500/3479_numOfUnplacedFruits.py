class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.tree = [0] * (4 * len(arr) + 1)

    def update(self, idx):
        self.tree[idx] = max(self.tree[idx << 1], self.tree[idx << 1 | 1])

    def build(self, idx, left, right):
        if left == right:
            self.tree[idx] = self.arr[left]
            return
        
        mid = (left + right) >> 1

        self.build(idx << 1, left, mid)
        self.build(idx << 1 | 1, mid + 1, right)

        self.update(idx)
    
    def assign(self, pos, val, idx, left, right):
        if pos < left or pos > right:
            return
        
        if left == right:
            self.tree[idx] = val
            return
        
        mid = (left + right) >> 1

        self.assign(pos, val, idx << 1, left, mid)
        self.assign(pos, val, idx << 1 | 1, mid + 1, right)

        self.update(idx)

    def first_larger(self, val, idx, left, right):
        if self.tree[idx] < val:
            return right + 1
        
        if left == right:
            return right
        
        mid = (left + right) >> 1
        i = self.first_larger(val, idx << 1, left, mid)

        if i <= mid:
            return i

        return self.first_larger(val, idx << 1 | 1, mid + 1, right)


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        unplaced = 0

        tree = SegmentTree(baskets)
        tree.build(1, 0, n - 1)

        for fruit in fruits:
            pos = tree.first_larger(fruit, 1, 0, n - 1)

            if pos == n:
                unplaced += 1
            else:
                tree.assign(pos, 0, 1, 0, n - 1)

        return unplaced
