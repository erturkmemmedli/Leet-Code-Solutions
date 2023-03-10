class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        nums = [-i for i in nums]
        stack = []
        result = 0
        for i, num in enumerate(nums):
            if not stack or num > stack[-1][0]:
                stack.append([num, i])
            else:
                idx = bisect.bisect_left(stack, [num, 0])
                result = max(result, i - stack[idx][1])
        return result
