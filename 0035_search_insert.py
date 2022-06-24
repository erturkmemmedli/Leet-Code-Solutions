class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        return self.binary_search(nums, target, left, right)
    
    def binary_search(self, nums, target, left, right):
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if left >= right:
            if nums[mid] > target:
                return left
            else:
                return left + 1
        if nums[mid] > target:
            return self.binary_search(nums, target, left, mid)
        if nums[mid] < target:
            return self.binary_search(nums, target, mid + 1, right)

# Alternative solution

class Solution1:
    def searchInsert(self, nums: List[int], target: int) -> int:
        mid = len(nums) // 2
        if nums[mid] == target:
            return mid
        if len(nums) == 1:
            if nums[mid] > target:
                return mid
            else:
                return mid + 1
        if nums[mid] > target:
            return self.searchInsert(nums[:mid], target)
        if nums[mid] < target:
            return mid + self.searchInsert(nums[mid:], target)
        
# Alternative solution

class Solution2:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if left == right:
                if nums[mid] > target: return mid
                else: return mid + 1
            if nums[mid] > target:
                right = mid
            if nums[mid] < target:
                left = mid + 1
