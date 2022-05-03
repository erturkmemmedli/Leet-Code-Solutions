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