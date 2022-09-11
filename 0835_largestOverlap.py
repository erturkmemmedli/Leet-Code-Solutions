from collections import defaultdict

class Solution:
    def c(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        pix1 = []
        pix2 = []
        for i in range(n):
            for j in range(n):
                if img1[i][j]: pix1.append((i,j))
                if img2[i][j]: pix2.append((i,j))
        directions = defaultdict(int)
        for a, b in pix1:
            for c, d in pix2:
                directions[(a-c, b-d)] += 1
        return max(directions.values()) if directions else 0
