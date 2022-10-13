class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1: return False
        subset_total = total // 2
        mxm = max(nums)
        if mxm > subset_total: return False
        elif mxm == subset_total: return True
        hashset = {subset_total}
        for num in nums:
            if num in hashset:
                return True
            for item in hashset.copy():
                hashset.add(item - num)
        return False
