class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        return len({val for key, val in Counter(s).items()}) == 1
