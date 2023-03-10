import heapq

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        heapq.heapify(nums)
        start = 1
        while nums:
            pop = heapq.heappop(nums)
            if pop < start:
                continue
            elif pop > start:
                return start
            else: 
                start += 1
        if pop < 0: 
            return 1
        else: 
            return pop + 1

# Alternative solution

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            j = nums[i] - 1
            if 0 <= j < len(nums) - 1 and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1
