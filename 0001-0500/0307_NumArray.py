class BinaryIndexedTree:
    def __init__(self, size):
        self.tree = [0] * size
    
    def getSum(self, index):
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= index & -index
        return result

    def sumRange(self, left, right):
        return self.getSum(right) - self.getSum(left - 1)

    def buildTree(self, index, value):
        while index < len(self.tree):
            self.tree[index] += value
            index += index & -index

class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.FenwickTree = BinaryIndexedTree(len(nums) + 1)
        for i in range(len(nums)):
            self.FenwickTree.buildTree(i + 1, self.nums[i])

    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        self.nums[index] = val
        self.FenwickTree.buildTree(index + 1, diff)

    def sumRange(self, left: int, right: int) -> int:
        return self.FenwickTree.sumRange(left + 1, right + 1)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

# Alternative solution (which gives TLE error)

class NumArray1:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefixSum = [nums[0]]
        for i in range(1, len(nums)):
            self.prefixSum.append(self.prefixSum[-1] + nums[i])

    def update(self, index: int, val: int) -> None:
        replaced = self.nums[index]
        diff = val - replaced
        self.nums[index] = val
        for i in range(index, len(self.nums)):
            self.prefixSum[i] += diff

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSum[right] - self.prefixSum[left - 1] if left > 0 else self.prefixSum[right]

# Alternative solution

class SegmentTreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None
        

class NumArray:
    def __init__(self, nums: List[int]):
        def createTree(nums, l, r):
            if l > r:
                return None
                
            if l == r:
                n = SegmentTreeNode(l, r)
                n.total = nums[l]
                return n
            
            mid = (l + r) // 2
            root = SegmentTreeNode(l, r)
            root.left = createTree(nums, l, mid)
            root.right = createTree(nums, mid + 1, r)
            root.total = root.left.total + root.right.total
            return root
        
        self.root = createTree(nums, 0, len(nums) - 1)

    def update(self, index: int, val: int) -> None:
        def updateVal(root, i, val):
            if root.start == root.end:
                root.total = val
                return val
        
            mid = (root.start + root.end) // 2
            
            if i <= mid:
                updateVal(root.left, i, val)
            else:
                updateVal(root.right, i, val)
            
            root.total = root.left.total + root.right.total
            return root.total
        
        return updateVal(self.root, index, val)

    def sumRange(self, left: int, right: int) -> int:
        def rangeSum(root, i, j):            
            if root.start == i and root.end == j:
                return root.total
            
            mid = (root.start + root.end) // 2

            if j <= mid:
                return rangeSum(root.left, i, j)
            elif i >= mid + 1:
                return rangeSum(root.right, i, j)
            else:
                return rangeSum(root.left, i, mid) + rangeSum(root.right, mid + 1, j)
        
        return rangeSum(self.root, left, right)
