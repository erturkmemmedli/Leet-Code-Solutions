class Solution:
    def twoSum(self, nums, target, exception, my_set):
        hashmap = {}
        for i in range(len(nums)):
            if i == exception:
                continue
            if nums[i] not in hashmap:
                hashmap[target - nums[i]] = i
            else:
                x = hashmap[nums[i]]
                pair = tuple(sorted([nums[exception], nums[i], nums[x]]))
                my_set.add(pair)
        return my_set
    
    def threeSum(self, nums):
        my_set = set()
        my_dict = {}
        for i in range(len(nums)):
            target = - nums[i]
            exception = i
            if target not in my_dict:
                my_dict[target] = True
                my_set = self.twoSum(nums, target, exception, my_set)
        return [list(i) for i in my_set]
