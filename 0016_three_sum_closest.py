class Solution:
    def threeSumClosest(self, nums, target):
        nums = sorted(nums)
        output = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            temp = nums[i] + nums[j] + nums[k]
            while j < k:
                if temp == target:
                    return temp
                temp = nums[i] + nums[j] + nums[k]
                if abs(temp - target) < abs(output - target):
                    output = temp
                if temp < target:
                    j += 1
                else:
                    k -= 1
        return output
