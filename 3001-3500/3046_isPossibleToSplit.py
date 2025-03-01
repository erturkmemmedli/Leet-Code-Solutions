class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        counter = {}

        for num in nums:
            counter[num] = counter.get(num, 0) + 1
            if counter[num] == 3:
                return False

        return True
