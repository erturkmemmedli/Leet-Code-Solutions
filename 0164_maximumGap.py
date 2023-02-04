class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        high, low = -inf, inf
        for num in nums:
            high = max(high, num)
            low = min(low, num)
        if n < 2 or high == low:
            return 0
        bucket = defaultdict(list)
        for num in nums:
            index = n - 2 if num == high else (num - low) * (n - 1) // (high - low)
            bucket[index].append(num)
        candidates = [[min(bucket[i]), max(bucket[i])] for i in range(n - 1) if bucket[i]]
        maxDiff = 0
        for i in range(1, len(candidates)):
            maxDiff = max(maxDiff, candidates[i][0] - candidates[i - 1][1])
        return maxDiff
