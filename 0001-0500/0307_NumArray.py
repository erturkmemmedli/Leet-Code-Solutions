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
