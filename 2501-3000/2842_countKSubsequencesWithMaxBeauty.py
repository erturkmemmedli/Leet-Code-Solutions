class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        c = Counter(s)

        if len(c) < k:
            return 0

        freq = list(c.values())
        total = sum(sorted(freq, reverse=True)[:k])
        memo = {}
        
        def backtrack(i, k, target):
            if k == 0:
                return int(target == 0)
            if i == len(freq):
                return 0

            if (i, k, target) in memo:
                return memo[(i, k, target)]
            
            ans = backtrack(i + 1, k, target)
            ans += backtrack(i + 1, k - 1, target - freq[i]) * freq[i]
            ans %= 1_000_000_007
            memo[(i, k, target)] = ans
            return ans

        return backtrack(0, k, total)
