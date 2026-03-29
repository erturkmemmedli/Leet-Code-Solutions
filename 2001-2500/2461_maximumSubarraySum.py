class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        window = set()
        curr = 0
        maximum = 0
        left = 0

        for right in range(len(nums)):
            while nums[right] in window:
                window.remove(nums[left])
                curr -= nums[left]
                left += 1
            
            window.add(nums[right])
            curr += nums[right]

            if len(window) > k:
                window.remove(nums[left])
                curr -= nums[left]
                left += 1
            
            if len(window) == k:
                maximum = max(maximum, curr)
            
        return maximum
