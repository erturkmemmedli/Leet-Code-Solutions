class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    count += 1
        return count

# Alternative solution

class Solution1:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dictionary = {}
        for num in nums:
            if num not in dictionary:
                dictionary[num] = 0
            else:
                dictionary[num] += 1
        count = 0
        for val in dictionary.values():
            if val:
                count += (val * (val + 1) // 2)
        return count

# Alternative solution

from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums):
        counter = Counter(nums)
        answer = 0
        for key, val in counter.items():
            if val > 1:
                answer += (val - 1) * val // 2
        return answer
