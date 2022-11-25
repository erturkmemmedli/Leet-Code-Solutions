class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        return min(self.helper(nums[:], True), self.helper(nums[:], False))

    def helper(self, nums, flag):
        move = 0
        for i in range(0, len(nums)-1):
            if flag:
                if nums[i+1] <= nums[i]:
                    difference = abs(nums[i] - nums[i+1]) + 1
                    nums[i] -= difference
                    move += difference
                flag = False
            else:
                if nums[i+1] >= nums[i]:
                    difference = abs(nums[i] - nums[i+1]) + 1
                    nums[i+1] -= difference
                    move += difference
                flag = True
        return move
