class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        c = Counter(nums)
        return all(v % 2 == 0 for v in c.values())
