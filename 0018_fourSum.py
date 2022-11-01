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
            if num not in hashset:
                hashset.add(num)
                ex3 = i
                trgt = target - num
                self.twoSum(nums, trgt, ex3, ex4, output)
            
    def fourSum(self, nums, target):
        output = set()
        hashset = set()
        for i, num in enumerate(nums):
            if num not in hashset:
                hashset.add(num)
                ex4 = i
                trgt = target - num
                self.threeSum(nums, trgt, ex4, output) 
        return [list(i) for i in output]

# Alternative solution

class Solution1:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = set()
        visited = set()
        for i in range(len(nums)):
            if nums[i] in visited:
                continue
            visited.add(nums[i])
            new_target = target - nums[i]
            possible = self.threeSum(nums, new_target, i)
            for a, b, c in possible:
                result.add(tuple(sorted([nums[i], a, b, c])))
        return result

    def threeSum(self, nums, target, ex):
        result = set()
        visited = set()
        for i in range(len(nums)):
            if i == ex or nums[i] in visited:
                continue
            visited.add(nums[i])
            new_target = target - nums[i]
            possible = self.twoSum(nums, new_target, ex, i)
            for a, b in possible:
                result.add(tuple(sorted([nums[i], a, b])))
        return result

    def twoSum(self, nums, target, ex1, ex2):
        dictionary = set()
        result = set()
        visited = set()
        for i, num in enumerate(nums):
            if i == ex1 or i == ex2 or num in visited:
                continue
            if num not in dictionary:
                dictionary.add(target - num)
            else:
                result.add(tuple(sorted([target - num, num])))
                visited.add(target - num)
                visited.add(num)
        return result

# Alternative solution

class Solution2:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def twoSum(first, second, nums, target):
            dictionary = set()
            visited = set()
            for num in nums:
                if num in visited:
                    continue
                if num not in dictionary:
                    dictionary.add(target - num)
                else:
                    result.append([first, second, target - num, num])
                    visited.add(target - num)
                    visited.add(num)
        nums.sort()
        visited = set()
        result = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i], nums[j]) in visited:
                    continue
                visited.add((nums[i], nums[j]))
                new_target = target - nums[i] - nums[j]
                twoSum(nums[i], nums[j], nums[j+1:], new_target)
        return result
