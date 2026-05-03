from itertools import pairwise

class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        res = []
        curr = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                curr += 1
            else:
                res.append(curr)
                curr = 1

        res.append(curr)
        output = max(res) // 2

        for i, j in pairwise(res):
            output = max(output, min(i, j))

        return output
