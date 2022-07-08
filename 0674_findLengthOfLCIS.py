class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        j, count, mxm = 1, 1, 1
        for i in range(len(nums)-1):
            if nums[j] > nums[i]:
                count += 1
                mxm = max(mxm, count)
            else:
                count = 1
            j += 1
        return mxm
