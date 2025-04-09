class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        c = sorted(Counter(nums).most_common(), key=lambda x: -x[0])
        if c[-1][0] < k:
            return -1
        if c[-1][0] == k:
            return len(c) - 1
        return len(c)
