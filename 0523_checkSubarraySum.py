class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hashmap = {0: 0}
        total = 0
        for i, num in enumerate(nums):
            total += num
            if total % k not in hashmap:
                hashmap[total % k] = i + 1
            elif i - hashmap[total % k] > 0:
                return True
        return False
