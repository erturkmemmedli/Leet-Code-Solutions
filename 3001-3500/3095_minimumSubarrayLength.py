class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        total = 0
        minimum = math.inf

        for num in nums:
            total |= num
        
        if total < k:
            return -1
        
        for i in range(len(nums)):
            val = nums[i]
            for j in range(i, len(nums)):
                val |= nums[j]
                if val >= k:
                    minimum = min(j - i + 1, minimum)
                    break
            
        return minimum
