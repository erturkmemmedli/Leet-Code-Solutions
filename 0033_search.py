class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        if nums[0] < nums[-1]:
            return self.binarySearchTarget(nums, target, left, right)
        index = self.binarySearchMinimum(nums, left, right)
        if nums[index] <= target <= nums[right]:
            result = self.binarySearchTarget(nums[index:], target, 0, right - index)
            return index + result if result >= 0 else -1
        else:
            return self.binarySearchTarget(nums[:index], target, left, index - 1)

    def binarySearchMinimum(self, nums, left, right):
        if left == right:
            return left
        mid = (left + right) // 2
        if nums[mid] >= nums[0]:
            return self.binarySearchMinimum(nums,  mid + 1, right)
        if nums[mid] < nums[0]:
            return self.binarySearchMinimum(nums, left, mid)

    def binarySearchTarget(self, nums, target, left, right):
        if left > right:
            return -1
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.binarySearchTarget(nums, target, left, mid - 1)
        else:
            return self.binarySearchTarget(nums, target, mid + 1, right)

# Alternative solution

class Solution1:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[left]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
