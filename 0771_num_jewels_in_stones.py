class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set()
        for j in jewels:
            jewel_set.add(j)
        count = 0
        for s in stones:
            if s in jewel_set:
                count += 1
        return count
