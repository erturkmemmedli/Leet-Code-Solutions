class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): return False
        if len(s) == 0: return True
        for _ in range(len(s)):
            s = s[-1] + s[:-1]
            if s == goal: return True
        return False
