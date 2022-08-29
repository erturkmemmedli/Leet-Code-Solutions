class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mxm_dist = mxm_dist=0
        for i in range(len(nums) - 1):
            mxm_dist = max(mxm_dist - 1, nums[i])
            if mxm_dist == 0:
                return False
        return True
