class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        count = 0
        total = 0

        for num in nums:
            total += num
            if total == 0:
                count += 1
                
        return count
