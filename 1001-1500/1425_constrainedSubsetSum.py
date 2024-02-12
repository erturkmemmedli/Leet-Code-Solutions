class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        heap = [(-nums[0], 0)]
        ans = nums[0]

        for i in range(1, len(nums)):
            while i - heap[0][1] > k:
                heappop(heap)
            
            curr = max(0, -heap[0][0]) + nums[i]
            ans = max(ans, curr)
            heappush(heap, (-curr, i))

        return ans

# Alternative solution

from sortedcontainers import SortedList

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        tree = SortedList([0])
        dp = [0] * len(nums)

        for i in range(len(nums)):
            dp[i] = nums[i] + tree[-1]
            tree.add(dp[i])

            if i >= k:
                tree.remove(dp[i - k])
            
        return max(dp)

# Alternative solution

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        queue = deque()
        dp = [0] * len(nums)

        for i in range(len(nums)):
            while queue and i - queue[0] > k:
                queue.popleft()
            
            dp[i] = (dp[queue[0]] if queue else 0) + nums[i]

            while queue and dp[queue[-1]] < dp[i]:
                queue.pop()
            
            if dp[i] > 0:
                queue.append(i)

        return max(dp)
