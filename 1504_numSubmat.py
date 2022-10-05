class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        count = 0
        for i in range(m):
            count += mat[i][0]
            for j in range(1, n):
                if mat[i][j]:
                    mat[i][j] = mat[i][j-1] + 1
                    count += mat[i][j]
        for r in range(m-1):
            for j in range(n):
                if mat[r][j]:
                    i = r + 1
                    top_down = mat[r][j]
                    while i < m and mat[i][j]:
                        top_down = min(top_down, mat[i][j])
                        count += top_down
                        i += 1
        return count
