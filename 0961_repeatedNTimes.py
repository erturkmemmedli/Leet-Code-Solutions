class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        myset = set()
        for num in nums:
            if num in myset:
                return num
            myset.add(num)
