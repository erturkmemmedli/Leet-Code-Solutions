import copy, random

class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        new_list = copy.deepcopy(self.nums)
        random.shuffle(new_list)
        return new_list

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

# Alternative solution

import random

class Solution1:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.copy = nums[:]

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        n = len(self.nums)
        for i in range(n):
            j = random.randint(0, n-1)
            self.copy[i], self.copy[j] = self.copy[j], self.copy[i]
        return self.copy
