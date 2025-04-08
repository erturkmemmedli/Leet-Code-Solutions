class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        hashmap = Counter(nums)
        current = 0
        step = 1

        for i in range(0, len(nums), 3):
            hashmap[nums[i]] -= 1
            if  hashmap[nums[i]] != 0:
                current = step
            
            if i + 1 < len(nums):
                hashmap[nums[i + 1]] -= 1
                if  hashmap[nums[i + 1]] != 0:
                    current = step

            if i + 2 < len(nums):
                hashmap[nums[i + 2]] -= 1
                if  hashmap[nums[i + 2]] != 0:
                    current = step
            
            step += 1
                
        return current
