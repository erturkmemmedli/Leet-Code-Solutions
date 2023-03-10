class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        mid = (len(nums) - 1) // 2
        if len(nums) == 1: return nums[mid]
        if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]: return nums[mid]
        if mid % 2:
            if nums[mid] == nums[mid-1]:
                return self.singleNonDuplicate(nums[mid+1:])
            else:
                return self.singleNonDuplicate(nums[:mid])
        else:
            if nums[mid] == nums[mid+1]:
                return self.singleNonDuplicate(nums[mid+2:])
            else:
                return self.singleNonDuplicate(nums[:mid-1])

# Alternative solution

class Solution:
    def singleNonDuplicate(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if (right - left + 1) % 4 == 1:
                if nums[mid] == nums[mid - 1]:
                    right = mid
                elif nums[mid] == nums[mid + 1]:
                    left = mid
                else:
                    return nums[mid]
            else:
                if nums[mid] == nums[mid - 1]:
                    left = mid + 1
                elif nums[mid] == nums[mid + 1]:
                    right = mid - 1
                else:
                    return nums[mid]
        return nums[left]
