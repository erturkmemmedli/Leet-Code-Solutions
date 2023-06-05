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

# Alternative solution

class MinHeap:
    def __init__(self, array):
        self.heap = array

    def push(self, num):
        self.heap.append(num)
        self.sift_up(num, len(self.heap) - 1)

    def pop(self):
        self.heap[0] = float('inf')
        min_element = self.sift_down()
        self.heap.pop()
        return min_element

    def sift_up(self, num, current_idx):
        while current_idx:
            if current_idx % 2 == 0:
                parent_idx = (current_idx - 2) // 2
            else:
                parent_idx = (current_idx - 1) // 2

            parent_node = self.heap[parent_idx]

            if parent_node > num:
                self.heap[current_idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[current_idx]
                current_idx = parent_idx
            else:
                break

    def sift_down(self):
        root_idx = 0
        root_value = self.heap[root_idx]

        while True:
            left_node_idx = root_idx * 2 + 1
            right_node_idx = root_idx * 2 + 2

            if left_node_idx >= len(self.heap):
                break

            elif right_node_idx >= len(self.heap):
                self.heap[root_idx], self.heap[left_node_idx] = self.heap[left_node_idx], self.heap[root_idx]
                return root_value
                        
            if self.heap[left_node_idx] < self.heap[right_node_idx]:
                self.heap[root_idx], self.heap[left_node_idx] = self.heap[left_node_idx], self.heap[root_idx]
                root_idx = left_node_idx
            else:
                self.heap[root_idx], self.heap[right_node_idx] = self.heap[right_node_idx], self.heap[root_idx]
                root_idx = right_node_idx

        last_node = self.heap[-1]
        self.heap[-1], self.heap[root_idx] = self.heap[root_idx], self.heap[-1]
        self.sift_up(last_node, root_idx)
        return root_value
            
    def get_min(self):
        return self.heap[0]

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = MinHeap([])

        for i in range(k):
            heap.push(nums[i])

        for i in range(k, len(nums)):
            if nums[i] > heap.get_min():
                heap.pop()
                heap.push(nums[i])

        return heap.get_min()
