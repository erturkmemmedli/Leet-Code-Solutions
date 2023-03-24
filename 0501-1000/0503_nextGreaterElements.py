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

# Alternative solution

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        idx = nums.index(max(nums))
        nums = nums[idx+1:] + nums[:idx+1]
        
        n = len(nums)
        stack = []
        output = [None] * n
        i = n - 1
        
        while i >= 0:
            while stack and stack[-1] <= nums[i]:
                stack.pop()
                
            output[i] = stack[-1] if stack else -1
            stack.append(nums[i])
            i -= 1
            
        return output[n-idx-1:] + output[:n-idx-1]
