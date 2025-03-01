class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        total = nums[0] + nums[1] + nums[2]
        a, b = nums[1], nums[2]
        
        for i in range(3, len(nums)):
            if nums[i] <= a or nums[i] <= b:
                if a < b:
                    b = nums[i]
                else:
                    a, b = b, nums[i]
                
                total = min(total, nums[0] + a + b)
        
        return total
