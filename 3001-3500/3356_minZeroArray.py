class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)

        if all(num == 0 for num in nums):
            return 0

        l, r = 1, len(queries)

        if not self.is_suitable(n, r, queries, nums):
            return -1

        while l < r:
            mid = l + (r - l) // 2

            if self.is_suitable(n, mid, queries, nums):
                r = mid
            else:
                l = mid + 1
        
        return l

    def is_suitable(self, n, k, queries, nums):
        diff = [0] * (n + 1)

        for i in range(k):
            l, r, val = queries[i]
            diff[l] += val
            diff[r + 1] -= val

        curr = 0

        for i in range(n):
            curr += diff[i]
            if curr < nums[i]:
                return False
        
        return True
