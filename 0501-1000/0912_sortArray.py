class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return sorted(nums)
        
# Alternative solution

class Solution1:
    def sortArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        return nums
        
# Alternative solution

import random

class Solution2:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        pivot = random.choice(nums)
        index = nums.index(pivot)
        less = [x for i, x in enumerate(nums) if x <= pivot and i != index]
        greater = [x for x in nums if x > pivot]
        return self.sortArray(less) + [pivot] + self.sortArray(greater)
        
# Alternative solution

from collections import deque

class Solution3:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        nums = self.merge_sort(deque(left), deque(right))
        return nums
        
    def merge_sort(self, left, right):
        output = []
        while left and right:
            if left[0] <= right[0]:
                output.append(left.popleft())
            else:
                output.append(right.popleft())
        if left:
            output += left
        else:
            output += right
        return output
