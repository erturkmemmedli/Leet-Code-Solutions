class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        stack = []
        count = 0
        for num in nums:
            if not stack:
                if num == 0:
                    continue
                else:
                    stack.append(1)
            else:
                if num == 1:
                    if stack[-1]:
                        stack[-1] += 1
                    else:
                        stack.append(1)
                else:
                    stack.append(0)
        if not stack: return 0
        maximum = stack[0]
        if (len(stack) == 1 and nums[0] == 0) or len(stack) == 2: return maximum
        if len(stack) == 1 : return maximum - 1            
        for i in range(2, len(stack)):
            maximum = max(maximum, stack[i] + stack[i-2])
        return maximum
