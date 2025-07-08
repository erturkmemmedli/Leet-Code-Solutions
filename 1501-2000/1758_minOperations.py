class Solution:
    def minOperations(self, s: str) -> int:
        key = count = 0

        for char in s:
            if int(char) == key:
                count += 1
            key ^= 1
        
        return min(count, len(s) - count)
