class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        decrease = False
        increase = False
        for i in range(1, len(nums)):
            if not decrease and not increase:
                if nums[i] > nums[i-1]: increase = True
                if nums[i] < nums[i-1]: decrease = True
                else: continue
            if increase:
                if nums[i] < nums[i-1]: return False
            if decrease:
                if nums[i] > nums[i-1]: return False
        return True
