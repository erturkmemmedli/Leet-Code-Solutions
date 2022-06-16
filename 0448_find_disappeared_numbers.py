class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = set(nums)
        res = []
        for i in range(1, len(nums)+1):
            if i not in s: res.append(i)
        return res
      
# Alternative solution

class Solution1:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            index = abs(nums[i])-1
            if nums[index] > 0:
                nums[index] *= -1
        result = []
        for i, num in enumerate(nums):
            if num > 0: result.append(i+1)
        return result
