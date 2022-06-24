class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        width = int(area ** 0.5)
        for i in range(width,0,-1):
            if area % i == 0:
                return [area // i, i]
