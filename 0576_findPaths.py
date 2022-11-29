class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        if m == 1 and n == 1: return 4
        result = 0
        self.hashmap = collections.defaultdict(int)
        for i in range(1, maxMove + 1):
            self.backtrack(m, n, i, startRow, startColumn)
            result += self.hashmap[(startRow, startColumn, i)]
        return result % 1000000007

    #@functools.lru_cache(None)
    def backtrack(self, m, n, move, row, col):
        # memoization
        if (row, col, move) in self.hashmap:
            return
        # base case
        if move == 1:
            if (row, col) in [(0, 0), (m-1, n-1), (0, n-1), (m-1, 0)]:
                if m == 1 or n == 1:
                    self.hashmap[(row, col, move)] = 3
                else:
                    self.hashmap[(row, col, move)] = 2
            elif (row in (0, m-1) and 0 < col < n-1) or (0 < row < m-1 and col in (0, n-1)):
                if m == 1 or n == 1:
                    self.hashmap[(row, col, move)] = 2
                else:
                    self.hashmap[(row, col, move)] = 1
            return
        else:
            for r, c in [row-1, col], [row+1, col], [row, col-1], [row, col+1]:
                if m > r >= 0 <= c < n:
                    self.backtrack(m, n, move - 1, r, c)
                    # using memoized data
                    self.hashmap[(row, col, move)] += self.hashmap[(r, c, move - 1)]
