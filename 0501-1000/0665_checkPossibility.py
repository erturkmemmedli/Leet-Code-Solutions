class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        flag = False
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                if flag:
                    return False
                if i == 1:
                    nums[i-1] = nums[i]
                else:
                    if nums[i-2] <= nums[i]:
                        nums[i-1] = nums[i]
                    else:
                         nums[i] = nums[i-1]
                flag = True
        return True
