class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = [0]
        output = [None] * len(nums)
        for i in range(1, len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                pop = stack.pop()
                output[pop] = nums[i]            
            stack.append(i)
        for i in range(0, len(nums)):
            if len(stack) == 1:
                break
            while nums[i] > nums[stack[-1]]:
                pop = stack.pop()
                output[pop] = nums[i]
        while stack:
            pop = stack.pop()
            output[pop] = -1
        return output
