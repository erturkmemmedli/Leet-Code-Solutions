from collections import Counter

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal) or len(s) == 1 or len(goal) == 1: return False
        c1, c2 = Counter(s), Counter(goal)
        if c1 - c2 or c2 - c1: return False
        if len(c1) == 1: return True
        count = 0
        for i, char in enumerate(s):
            if char != goal[i]:
                count += 1
        return count == 2 or (count == 0 and max(c1.values()) > 1)
