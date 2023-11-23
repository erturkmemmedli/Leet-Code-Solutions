class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        memo = {}
        result = 0

        def dp(step, mask):
            if step == m * n:
                return 1

            row, col = divmod(step, m)
            result = 0
            
            if (step, mask) in memo:
                return memo[(step, mask)]
            
            for color in {'1', '2', '3'} - {mask[col], mask[col-1]}:
                new_mask = mask[:col] + color + mask[col+1:]
                result += dp(step+1, new_mask)
                result %= (10**9 + 7)
            
            memo[(step, mask)] = result
            return result

        return dp(0, "0" * (m + 1))
