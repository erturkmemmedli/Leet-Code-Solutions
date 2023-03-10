class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        return self.binarySearch(nums, left, right)

    def binarySearch(self, nums, left, right):
        if right - left <= 1:
            return min(nums[left], nums[right])
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            return self.binarySearch(nums, mid, right)
        elif nums[mid] < nums[right]:
            return self.binarySearch(nums, left, mid)
        elif nums[mid] < nums[left]:
            if nums[mid] >= nums[mid - 1]:
                return self.binarySearch(nums, left, mid)
            return self.binarySearch(nums, mid, right)
        elif nums[mid] > nums[left]:
            return self.binarySearch(nums, left, mid)
        else:
            return min(self.binarySearch(nums, left, mid), self.binarySearch(nums, mid, right))
