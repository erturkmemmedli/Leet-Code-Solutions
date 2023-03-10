class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs, key = lambda x: x[1])
        chain_length = 1
        y_prev = pairs[0][1]
        for i in range(1, len(pairs)):
            x, y = pairs[i]
            if x > y_prev:
                chain_length += 1
                y_prev = y
                continue
        return chain_length
