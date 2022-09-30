class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        answer = []
        i = 0
        j = 0
        while i < m and j < n:
            answer.append(mat[i][j])
            if (i + j) % 2 == 1:
                if j == 0 or i == m - 1:
                    if i + 1 < m:
                        i += 1
                    else:
                        j += 1
                else:
                    i += 1
                    j -= 1
            else:
                if i == 0 or j == n - 1:
                    if j + 1 < n:
                        j += 1
                    else:
                        i += 1
                else:
                    i -= 1
                    j += 1
        return answer
