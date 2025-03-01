class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        count_op = 0
        target = nums[0] + nums[1]

        for i in range(0, len(nums), 2):
            if i + 1 < len(nums) and nums[i] + nums[i + 1] == target:
                count_op += 1
            else:
                break

        return count_op
