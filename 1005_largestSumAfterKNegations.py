class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        for i in range(len(nums)):
            if k == 0:
                break
            if nums[i] < 0:
                nums[i] = -nums[i]
                k -= 1
            elif nums[i] == 0:
                k = 0
                break
            else:
                if k % 2 != 0:
                    if i and nums[i-1] < nums[i]:
                        nums[i-1] = -nums[i-1]
                    else:
                        nums[i] = -nums[i]
                k = 0
                break
        if k and k % 2 != 0:
            nums[-1] = -nums[-1]
        return sum(nums)                           
