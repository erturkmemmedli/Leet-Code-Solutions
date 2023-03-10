class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        output = []
        x = 0
        y = 0
        while y < len(s):
            if s[x] == s[y]:
                y += 1
            else:
                if y - x >= 3:
                    output.append([x, y-1])
                x = y
        if y - x >= 3:
            output.append([x, y-1])
        return output
