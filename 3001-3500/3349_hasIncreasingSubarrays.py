class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        for i in range(max(len(nums) - 2 * k + 1, 0)):
            for j in range(i, i + k - 1):
                if nums[j + 1] <= nums[j] or nums[j + k + 1] <= nums[j + k]:
                    break
            else:
                return True
            
        return False
