class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        starting, ending = [], []
        for i in range(len(start)):
            if start[i] != 'X':
                starting.append((i, start[i]))
            if end[i] != 'X':
                ending.append((i, end[i]))
        while starting and ending:
            idx1, char1 = starting.pop()
            idx2, char2 = ending.pop()
            if char1 != char2:
                return False
            elif char1 == 'L' and idx1 < idx2:
                return False
            elif char2 == 'R' and idx1 > idx2:
                return False
        if starting or ending:
            return False
        return True
