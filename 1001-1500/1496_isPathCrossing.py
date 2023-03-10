class Solution:
    def isPathCrossing(self, path: str) -> bool:
        S = set()
        x = 0
        y = 0
        S.add((x,y))
        for dir in path:
            if dir == 'N':
                y += 1
            if dir == 'S':
                y -= 1
            if dir == 'E':
                x += 1
            if dir == 'W':
                x -= 1
            if (x,y) in S:
                return True
            else:
                S.add((x,y))
        return False
