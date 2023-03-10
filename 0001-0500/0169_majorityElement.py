class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
      
# Alternative solution

from collections import Counter

class Solution1:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        mxm = max(counter.values())
        for k, v in counter.items():
            if v == mxm:
                return k
              
# Alternative solution

class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        majority = nums[0]
        count = 0
        for num in nums:
            if num == majority:
                count += 1
            elif count:
                count -= 1
            elif not count:
                majority = num
                count += 1
        return majority
