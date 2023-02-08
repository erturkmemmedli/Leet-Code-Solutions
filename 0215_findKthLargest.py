from heapq import heapify, heappop

class Solution:
    def findKthLargest(self, nums: List[List[int]], k: int) -> int:
        neg_heap = False
        if len(nums) // 2 >= k:
            nums[:] = [-i for i in nums]
            neg_heap = True
        else:
            k = len(nums) - k + 1
        heapify(nums)
        for _ in range(k-1):
            heappop(nums)
        pop = heappop(nums)
        return pop if not neg_heap else -pop
    
# Alternative solution

import random

class Solution1:
    def findKthLargest(self, nums: List[List[int]], k: int) -> int:
        if not nums: return
        pivot = random.choice(nums)
        left = [i for i in nums if i < pivot]
        mid = [i for i in nums if i == pivot]
        right = [i for i in nums if i > pivot]
        l, m, r = len(left), len(mid), len(right)
        if k-1 < r:
            return self.findKthLargest(right, k)
        k -= r
        if k-1 < m:
            return mid[0]
        k -= m
        return self.findKthLargest(left, k)
    
# Alternative solution

class Solution2:
    def findKthLargest(self, nums: List[List[int]], k: int) -> int:
        return sorted(nums)[-k]

# Alternative solution

# This solution gives TLE (Time Limit Exceeded) error beacuse construction of BST is O(nlogn) at best and O(n^2) at worst.
# And for worst case, i.e. for sorted or inversely sorted array, time complexity of the construction of BST will be O(n^2).
# Although solution can be improved by balancing tree with AVL Tree or Red-Black Tree algorithms, it can also give O(nlogn) at best.
# I just write it down here because maybe I can improve it via one of the abovementioned algorithms one day.

class BST:
    def __init__(self, val, left_count, right_count, left, right):
        self.val = val
        self.left = None
        self.right = None
        self.left_count = 0
        self.right_count = 0

class Solution:
    def findKthLargest(self, nums: List[List[int]], k: int) -> int:
        tree = None
        for num in nums:
            tree = self.constructTree(tree, num)
        return self.traverse(tree, k, len(nums))
        
    def constructTree(self, tree, num):
        if not tree:
            return BST(num, 0, 0, None, None)
        elif num <= tree.val:
            tree.left_count += 1
            tree.left = self.constructTree(tree.left, num)
        elif num > tree.val:
            tree.right_count += 1
            tree.right = self.constructTree(tree.right, num)
        return tree
    
    def traverse(self, tree, k, n):
        if tree.right_count == k-1:
            return tree.val
        elif tree.right_count > k-1:
            return self.traverse(tree.right, k, tree.right_count)
        else:
            return self.traverse(tree.left, k-tree.right_count-1, tree.left_count)

# Alternative solution

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in range(k):
            heapq.heappush(heap, nums[i])
        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, nums[i])
        return heap[0]
