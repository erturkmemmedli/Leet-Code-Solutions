class Solution(object):
    def find132pattern(self, nums):
        stack = []
        k = - float('inf')
        for i in range(len(nums)-1, -1 , -1):
            if nums[i] < k:
                return True
            while stack != [] and stack[-1] < nums[i]:
                k = stack.pop()
            stack.append(nums[i])
        return False

# Alternative solution

class Solution1:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        mini, maxi = None, None
        for num in nums:
            if mini == None or (maxi == None and num <= mini):
                mini = num
            elif (maxi == None and num > mini) or num > maxi:
                maxi = num
                while stack:
                    if num <= stack[-1][0]:
                        break
                    elif stack[-1][0] < num < stack[-1][1]:
                        return True
                    else:
                        stack.pop()
            elif mini < num < maxi:
                return True
            elif num < mini:
                stack.append([mini, maxi])
                mini = num
                maxi = None
        return False
