class Solution:
    def twoSum(self, nums, target, ex3, ex4, output):
        hashmap = {}
        for i, num in enumerate(nums):
            if i == ex3 or i == ex4:
                continue
            if num not in hashmap:
                hashmap[target - num] = i
                continue
            if hashmap[num] == None:
                continue
            else:
                output.add(tuple(sorted([nums[ex4], nums[ex3], nums[hashmap[num]], nums[i]])))
                hashmap[num] = None

    def threeSum(self, nums, target, ex4, output):
        hashset = set()
        for i, num in enumerate(nums):
            if i == ex4:
                continue
            if i not in hashset:
                hashset.add(i)
                ex3 = i
                trgt = target - num
                self.twoSum(nums, trgt, ex3, ex4, output)
            
    def fourSum(self, nums, target):
        output = set()
        hashset = set()
        for i, num in enumerate(nums):
            if i not in hashset:
                hashset.add(i)
                ex4 = i
                trgt = target - num
                self.threeSum(nums, trgt, ex4, output) 
        return [list(i) for i in output]
