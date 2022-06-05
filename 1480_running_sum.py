class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if i:
                nums[i] += nums[i-1]
        return nums

# Alternative solution

class Solution1:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = [nums[0]]
        for i in range(1, len(nums)):
            result.append(nums[i] + result[i-1])
        return result
