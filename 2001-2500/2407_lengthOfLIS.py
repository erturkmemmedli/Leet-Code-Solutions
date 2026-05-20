class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * 2 * n

    def query(self, left, right):
        left += self.n
        right += self.n
        answer = 0
        while left < right:
            if left & 1:
                answer = max(answer, self.tree[left])
                left += 1
            if right & 1:
                right -= 1
                answer = max(answer, self.tree[right])
            left >>= 1
            right >>= 1
        return answer

    def update(self, idx, val):
        idx += self.n
        self.tree[idx] = val
        while idx > 1:
            idx >>= 1
            self.tree[idx] = max(self.tree[idx * 2], self.tree[idx * 2 + 1])

class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        n = max(nums)
        answer = 1
        segment = SegmentTree(n)
        for num in nums:
            num -= 1
            premax = segment.query(max(0, num - k), num)
            answer = max(answer, premax + 1)
            segment.update(num, premax + 1)
        return answer

# Alternative solutoin (which gives TLE error)

class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i+1):
                if 0 < nums[i] - nums[j] <= k:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
