class Solution:
    def minFlips(self, target: str) -> int:
        count = 0
        last_bit = target[0]
        for bit in target:
            if last_bit == bit:
                continue
            else:
                count += 1
                last_bit = bit
        return count if target[0] == "0" else count + 1
