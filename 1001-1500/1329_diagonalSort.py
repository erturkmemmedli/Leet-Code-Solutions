from collections import defaultdict

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        D = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                D[i-j].append(mat[i][j])
        for key in D.keys():
            D[key].sort(reverse = True)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j] = D[i-j].pop()
        return mat
