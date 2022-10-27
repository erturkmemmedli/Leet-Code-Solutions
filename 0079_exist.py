class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    self.visited = set()
                    if self.dfs(board, m, n, word[1:], i, j):
                        return True
        return False

    def dfs(self, board, m, n, word, r, c):
        if (r, c) not in self.visited:
            self.visited.add((r, c))
            if not word:
                return True
            for row, col in (r,c-1), (r,c+1), (r-1,c), (r+1,c):
                if m > row >= 0 <= col < n:
                    if board[row][col] == word[0]:
                        if self.dfs(board, m, n, word[1:], row, col):
                            return True
            self.visited.remove((r, c))
