class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        overall_array = []
        for i in range(len(nums)):
            overall_array.append(nums[i])
            for j in range(i+1, len(nums)):
                overall_array.append(nums[j] + overall_array[-1])
        overall_array.sort()
        return sum(overall_array[left-1:right]) % (10**9+7)
