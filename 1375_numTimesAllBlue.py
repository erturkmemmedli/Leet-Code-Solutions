class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        maximum, difference, minimum, prefix_aligned = None, None, 1, 0
        for flip in flips:
            if flip == minimum and not maximum:
                prefix_aligned += 1
                minimum += 1
                continue
            if not maximum:
                maximum, difference = flip, flip - minimum
            else:
                if flip < maximum:
                    difference -= 1
                else:
                    difference = flip - maximum - 1 + difference
                    maximum = flip
                if difference == 0:
                    prefix_aligned += 1
                    minimum = maximum + 1
                    maximum, difference = None, None
        return prefix_aligned
