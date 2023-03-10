class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        wpi = 0
        balance = 0
        hashmap = {0: -1}
        for i, hour in enumerate(hours):
            balance += 1 if hour > 8 else -1
            if balance not in hashmap:
                hashmap[balance] = i
            if balance - 1 in hashmap:
                wpi = max(wpi, i - hashmap[balance - 1])
        return wpi if balance <= 0 else len(hours)
