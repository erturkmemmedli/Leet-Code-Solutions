class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        maxList = []
        for i, num in enumerate(nums):
            while queue and queue[-1][1] < num:
                queue.pop()
            queue.append((i, num))
            if i < k - 1:
                continue
            maxList.append(queue[0][1])
            if i - queue[0][0] == k - 1:
                queue.popleft()
        return maxList
