class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = collections.Counter(nums)
        result = []
        n = len(nums) // 3
        for key, val in c.items():
            if val > n:
                result.append(key)
        return result
