class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        window = {}
        left = 0
        right = 0
        result = 0
        for num in nums:
            window[num] = window.get(num, 0) + 1
            if len(window) == k + 1:
                del window[nums[right]]
                right += 1
                left = right
            if len(window) == k:
                while window[nums[right]] > 1:
                    window[nums[right]] -= 1
                    right += 1
                result += right - left + 1
        return result
