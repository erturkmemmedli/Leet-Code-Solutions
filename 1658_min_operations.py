class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        summ = sum(nums)
        target = summ - x
        if target < 0: return -1
        if target == 0: return len(nums)
        result, left, right, temp = 0, 0, 0, 0
        while right < len(nums):
            if temp == target:
                result = max(result, right - left)
                temp -= nums[left]
                left += 1
            elif temp < target:
                temp += nums[right]
                if temp <= target:
                    right += 1
            elif temp > target:
                temp -= nums[left]
                left += 1
                if temp <= target or left >= right:
                    right += 1
        if temp == target:
            result = max(result, right - left)
        return -1 if not result else len(nums) - result
