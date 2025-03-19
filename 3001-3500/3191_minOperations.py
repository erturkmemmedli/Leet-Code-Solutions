class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        i = 0

        while i < len(nums) - 2:
            if nums[i] == 1:
                i += 1
                continue
            
            nums[i] ^= 1
            nums[i + 1] ^= 1
            nums[i + 2] ^= 1
            i += 1
            count += 1

        return -1 if nums[-2] == 0 or nums[-1] == 0 else count
