class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        minimum = k
        black = 0

        for i, color in enumerate(blocks):
            if i < k:
                if color == 'B':
                    black += 1
                if i == k - 1:
                    minimum = min(minimum, k - black)
                continue

            if blocks[i - k] == 'B':
                black -= 1
            if color == 'B':
                black += 1

            minimum = min(minimum, k - black)
            
        return minimum
