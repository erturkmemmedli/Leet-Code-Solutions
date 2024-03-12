class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        # full rotation
        if mat == target:
            return True
        # reverse rotation:
        mat_rot = []
        for m in mat[::-1]:
            mat_rot.append(m[::-1])
        if mat_rot == target:
            return True
        # left rotation
        mat_rot = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                mat_rot[i][j] = mat[n-j-1][i]
        if target == mat_rot:
            return True
        # right rotation
        mat_rot = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                mat_rot[i][j] = mat[j][n-i-1]
        if target == mat_rot:
            return True
        # otherwise
        return False
