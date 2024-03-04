class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        sorted_mat = sorted([(i, j) for i, j in product(range(m), range(n))], key = lambda x: mat[x[0]][x[1]])
        rows = [0] * m
        cols = [0] * n
        i = 0

        while i < len(sorted_mat):
            updatable = {}

            r, c = sorted_mat[i]
            longest = max(rows[r] + 1, cols[c] + 1)
            updatable[(r, c)] = longest
            i += 1

            while i < len(sorted_mat) and mat[sorted_mat[i][0]][sorted_mat[i][1]] == mat[sorted_mat[i-1][0]][sorted_mat[i-1][1]]:
                r, c = sorted_mat[i]
                longest = max(rows[r] + 1, cols[c] + 1)
                updatable[(r, c)] = longest
                i += 1
            
            for (row, col), longest in updatable.items():
                rows[row] = max(rows[row], longest)
                cols[col] = max(cols[col], longest)

        return max(max(rows), max(cols))

# Alternative solution (which gives TLE error)

class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        memo = {}

        def backtrack(r, c):
            if (r, c) in memo:
                return memo[(r, c)]
            
            ans = 1

            for row in range(m):
                if row != r and mat[row][c] > mat[r][c]:
                    ans = max(ans, 1 + backtrack(row, c))
            
            for col in range(n):
                if col != c and mat[r][col] > mat[r][c]:
                    ans = max(ans, 1 + backtrack(r, col))

            memo[(r, c)] = ans
            return ans

        max_path = 0

        for i in range(m):
            for j in range(n):
                max_path = max(max_path, backtrack(i, j))

        return max_path
