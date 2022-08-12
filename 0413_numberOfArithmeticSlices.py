class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        slices = []
        count = 1
        i = 1
        while i < len(nums):
            if count == 1:
                diff = nums[i] - nums[i-1]
                count += 1
                i += 1
            elif nums[i] - nums[i-1] == diff:
                count += 1
                i += 1
            else:
                if count >= 3:
                    slices.append(count)
                count = 1
        if count >= 3:
            slices.append(count)
        return sum([(i-2)*(i-1)//2 for i in slices])
