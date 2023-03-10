class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        dp = [inf for _ in range(len(books) + 1)]
        dp[0] = 0
        for i in range(1, len(books) + 1):
            width, height, j = shelfWidth, 0, i - 1
            while j >= 0 and width - books[j][0] >= 0:
                width -= books[j][0]
                height = max(height, books[j][1])
                dp[i] = min(dp[i], dp[j] + height)
                j -= 1
        return dp[-1]
