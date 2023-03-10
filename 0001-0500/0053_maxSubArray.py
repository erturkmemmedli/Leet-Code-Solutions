class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        summ = 0
        for num in nums:
            summ += num
            if summ < 0:
                result = max(result, summ)
                summ = 0
            else:
                result = max(result, summ)
        return result

# Alternative solution

class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = nums[0]
        temp = 0
        for i in range(len(nums)):
            if maximum <= 0 and nums[i] <= 0:
                maximum = max(maximum, nums[i])
                continue
            if nums[i] > 0:
                temp += nums[i]
                maximum = max(maximum, temp)
            if nums[i] < 0:
                if temp + nums[i] > 0:
                    temp += nums[i]
                else:
                    temp = 0
        return maximum
