import random
from collections import defaultdict

class Solution:
    def __init__(self, nums: List[int]):
        self.dictionary = defaultdict(list)
        for i, num in enumerate(nums):
            self.dictionary[num].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.dictionary[target])

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
