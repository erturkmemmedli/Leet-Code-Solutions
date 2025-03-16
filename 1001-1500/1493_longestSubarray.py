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

# Alternative solution

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero_count = 0
        left = 0
        answer = 0

        for right in range(len(nums)):
            while zero_count == 1 and nums[right] == 0:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            if nums[right] == 0:
                zero_count += 1
            answer = max(answer, right - left)
        
        return answer
