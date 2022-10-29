class Solution:
    def isRobotBounded(self, instructions: str) -> bool: 
        x, y, dx, dy = 0, 0, 0, 1
        for token in instructions:
            if token == 'L':
                dx, dy = -dy, dx
            if token == 'R':
                dx, dy = dy, -dx
            if token == 'G':
                x, y = x + dx, y + dy
        return (x == 0 and y == 0) or not (dx == 0 and dy == 1)
