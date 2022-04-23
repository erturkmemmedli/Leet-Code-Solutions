class Solution(object):

    def twoSum(self, nums, target):
        dictionary = {} 
        for i in range(len(nums)):
            if nums[i] not in dictionary:
                dictionary[target - nums[i]] = i	
            else:
                return [i, dictionary[nums[i]]]
