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
