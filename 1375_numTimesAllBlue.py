class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        stack = []
        minimum = 1
        prefix_aligned = 0
        for flip in flips:
            if flip == minimum and not stack:
                prefix_aligned += 1
                minimum += 1
                continue
            if not stack:
                stack = [flip, flip - minimum]
            else:
                if flip < stack[0]:
                    stack[1] -= 1
                else:
                    stack[1] = flip - stack[0] - 1 + stack[1]
                    stack[0] = flip
                if stack[1] == 0:
                    prefix_aligned += 1
                    minimum = stack[0] + 1
                    stack = []
        return prefix_aligned
