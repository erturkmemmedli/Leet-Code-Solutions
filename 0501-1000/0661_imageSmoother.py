class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        new_img = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                nominator = img[i][j]
                denominator = 1

                for r, c in (i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1):
                    if m > r >= 0 <= c < n:
                        nominator += img[r][c]
                        denominator += 1
                    
                new_img[i][j] = nominator // denominator

        return new_img
