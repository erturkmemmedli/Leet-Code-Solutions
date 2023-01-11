class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        self.counts = [0] * len(nums)
        self.mergeSort(list(enumerate(nums)))
        return self.counts

    def mergeSort(self, nums):
        mid = len(nums) // 2
        if mid:
            left, right = self.mergeSort(nums[:mid]), self.mergeSort(nums[mid:])
            for i in range(len(nums)-1, -1, -1):
                if not right or left and right[-1][1] < left[-1][1]:
                    self.counts[left[-1][0]] += len(right)
                    nums[i] = left.pop()
                else:
                    nums[i] = right.pop()
        return nums
      
# Alternative solution

from sortedcontainers import SortedList

class Solution1:
    def countSmaller(self, nums: List[int]) -> List[int]:
        tree = SortedList()
        result = []
        for num in nums[::-1]:
            index = bisect_left(tree, num)
            result.append(index)
            tree.add(num)
        return result[::-1]

# Alternative solution

class BinaryIndexedTree:
    def __init__(self, size):
        self.tree = [0] * (size + 1)

    def update(self, idx):
        while idx < len(self.tree):
            self.tree[idx] += 1
            idx += idx & -idx

    def sum(self, idx):
        s = 0
        while idx > 0:
            s += self.tree[idx]
            idx -= idx & -idx
        return s

class Solution2:
    def countSmaller(self, nums: List[int]) -> List[int]:
        hashTable = {v: i for i, v in enumerate(sorted(set(nums)))}
        tree = BinaryIndexedTree(len(hashTable))
        result = []
        for i in range(len(nums) - 1, -1, -1):
            result.append(tree.sum(hashTable[nums[i]]))
            tree.update(hashTable[nums[i]] + 1)
        return result[::-1]
