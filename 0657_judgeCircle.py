class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x, y = 0, 0
        for direction in moves:
            if direction == 'L':
                x -= 1
            if direction == 'R':
                x += 1
            if direction == 'D':
                y -= 1
            if direction == 'U':
                y += 1
        return not (x or y)
      
# Alternative solution

from collections import Counter

class Solution1:
    def judgeCircle(self, moves: str) -> bool:
        count = Counter(moves)
        return count['L'] == count['R'] and count['D'] == count['U']
