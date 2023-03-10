class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums.sort()
        prev, curr = 0, nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                curr += nums[i]
            elif nums[i] == nums[i-1] + 1:
                temp = prev
                prev = max(prev, curr)
                curr = temp + nums[i]
            else:
                prev = max(prev, curr)
                curr = prev + nums[i]
        return max(prev, curr)
