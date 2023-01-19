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

# Alternative solution

class Solution1:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.output = set()
        for i in range(len(nums)):
            if i == 0:
                self.twoSum(nums[1:], -nums[0])
            elif nums[i] != nums[i-1]:
                self.twoSum(nums[:i] + nums[i+1:], -nums[i])
        return self.output
                    
    def twoSum(self, nums, target):
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] + nums[j] > target:
                j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                self.output.add(tuple(sorted([-target, nums[i], nums[j]])))
                i += 1
                j -= 1

# Alternative solution

class Solution:
    def threeSum(self, nums):
        self.triplets = []
        nums.sort()
        for i in range(len(nums) - 2):
            if not self.triplets or nums[i] != self.triplets[-1][0]:
                self.twoSum(nums, i + 1, -nums[i])
        return self.triplets
        
    def twoSum(self, nums, index, target):
        i, j = index, len(nums) - 1
        while i < j:
            if nums[i] + nums[j] == target:
                small, big = nums[i], nums[j]
                self.triplets.append([-target, small, big])
                i += 1
                while nums[i] == small and i < j:
                    i += 1
                j -= 1
                while nums[i] == big and i < j:
                    j -= 1
            elif nums[i] + nums[j] > target:
                j -= 1
            else:
                i += 1
