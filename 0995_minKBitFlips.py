class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        result = 0
        current = 0
        n = len(nums)

        for i in range(len(nums)):
            if i >= k and nums[i - k] > 1:
                nums[i - k] -= 2
                current -= 1

            if current & 1 ^ nums[i] == 0:
                if i + k > n:
                    return -1
                
                nums[i] += 2
                current += 1
                result += 1

        return result
