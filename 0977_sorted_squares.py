class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([num ** 2 for num in nums])
   
# Alternative solution

class Solution1:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for index in range(len(nums)):
            if nums[index] < 0:
                nums[index] *= -1
            else:
                break
        result = []
        if index > 0 and nums[index] > abs(nums[index - 1]):
            i = index - 1
            j = index - 1
        else:
            i = index
            j = index
        while i >= 0 and j < len(nums):
            if i == j:
                result.append(nums[i] ** 2)
                i -= 1
                j += 1
                continue
            if nums[i] <= nums[j]:
                result.append(nums[i] ** 2)
                i -= 1
            else:
                result.append(nums[j] ** 2)
                j += 1
        if i < 0:
            for k in range(j, len(nums)):
                result.append(nums[k] ** 2)
        if j >= len(nums):
            for k in range(i, -1, -1):
                result.append(nums[k] ** 2)
        return result
