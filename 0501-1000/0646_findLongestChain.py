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

# Alternative solution

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        stack = []

        for pair in pairs:
            i = bisect_left(stack, pair[0])

            if i == len(stack):
                stack.append(pair[1])
            else:
                stack[i] = min(stack[i], pair[1])

        return len(stack)
