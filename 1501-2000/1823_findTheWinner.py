class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = collections.deque(list(range(1, n + 1)))
        while len(queue) > 1:
            for _ in range(k - 1):
                queue.append(queue.popleft())
            queue.popleft()
        return queue[0]
