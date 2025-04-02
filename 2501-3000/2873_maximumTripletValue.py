class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_val = 0
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    max_val = max(max_val, (nums[i] - nums[j]) * nums[k])
        return max_val
