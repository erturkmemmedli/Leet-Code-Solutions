class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return self.binarySearch(nums, target, 0, len(nums) - 1)

    def binarySearch(self, nums, target, left, right):
        if left > right:
            return -1, -1
        mid = (left + right) // 2
        if nums[mid] > target:
            return self.binarySearch(nums, target, left, mid - 1)
        elif nums[mid] < target:
            return self.binarySearch(nums, target, mid + 1, right)
        else:
            return self.LeftSearch(nums, target, left, mid), self.RightSearch(nums, target, mid, right)

    def LeftSearch(self, nums, target, left, right):
        if left == right or left == right - 1:
            return right if nums[left] != target else left
        mid = (left + right) // 2
        if nums[mid] == target:
            return self.LeftSearch(nums, target, left, mid)
        if nums[mid] < target:
            return self.LeftSearch(nums, target, mid + 1, right)

    def RightSearch(self, nums, target, left, right):
        if left == right or left == right - 1:
            return left if nums[right] != target else right
        mid = (left + right) // 2
        if nums[mid] > target:
            return self.RightSearch(nums, target, left, mid - 1)
        if nums[mid] == target:
            return self.RightSearch(nums, target, mid, right)

# Alternative solution

class Solution1:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target)
        return [-1, -1] if left == right else [left, right - 1]

# Alternative solution

class Solution:
    def searchRange(self, nums, target):
        result = [-1, -1]
        result[0] = self.binarySearch(nums, target, True)
        result[1] = self.binarySearch(nums, target, False)
        return result
        
    def binarySearch(self, nums, target, findFirstIndex):
        targetIndex = -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                targetIndex = mid
                if findFirstIndex:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return targetIndex
