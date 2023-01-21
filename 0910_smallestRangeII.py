class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        mnm, mxm = nums[0], nums[-1]
        ans = mxm - mnm
        for i in range(len(nums) - 1):
            a, b = nums[i], nums[i + 1]
            ans = min(ans, max(mxm - k, a + k) - min(mnm + k, b - k))
        return ans
