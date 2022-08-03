from collections import deque

class Solution:
    def findUnsortedSubarray(self, nums):
        maximum = nums[0]
        output = 0
        problem = len(nums)
        for i in range(1, len(nums)):
            if maximum <= nums[i]:
                maximum = nums[i]
            else:
                problem = min(problem, i)
                temp = problem - 1
                while temp >= 0 and nums[temp] > nums[i]:
                    problem = temp
                    temp -= 1
                output = i - problem + 1
        return output
    
# Alternative solution

class Solution1:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        start, end, highest, stack = len(nums), len(nums) - 1, -float('inf'), []
        for i, num in enumerate(nums):
            if not stack:
                stack.append(num)
            else:
                if num >= stack[-1]:
                    stack.append(num)
                    if num < highest:
                        end = i
                else:
                    while stack and stack[-1] > num:
                        highest = max(highest, stack.pop())
                    stack.append(num)
                    start = min(start, len(stack) - 1)
                    end = i
        return end - start + 1
