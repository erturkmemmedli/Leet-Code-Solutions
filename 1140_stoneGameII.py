class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        memo = {}
        start = 0
        M = 1
        return self.minimax(piles, memo, n, start, M)
    
    def minimax(self, piles, memo, n, start, M):
        if start >= n:
            return 0
        if n - start <= 2 * M:
            return sum(piles[start:])
        if (start, M) in memo:
            return memo[(start, M)]
        alice_score = 0
        total_score = sum(piles[start:])
        for i in range(1, 2 * M + 1):
            bob_score = self.minimax(piles, memo, n, start + i, max(i, M))
            alice_score = max(alice_score, total_score - bob_score)
        memo[(start, M)] = alice_score
        return alice_score
