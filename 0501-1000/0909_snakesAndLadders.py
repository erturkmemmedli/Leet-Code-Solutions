class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        visited = set()
        queue = collections.deque([(1, 0)])
        while queue:
            position, move = queue.popleft()
            row, col = self.determineRowColumn(n, position)
            if board[row][col] != -1:
                position = board[row][col]
            if position == n * n:
                return move
            for i in range(1, 7):
                newPosition = position + i
                if newPosition <= n * n and newPosition not in visited:
                    visited.add(newPosition)
                    queue.append((newPosition, move + 1))
        return -1   

    def determineRowColumn(self, n, position):
        r, c = divmod(position - 1, n)
        if r % 2 == 0:
            return n - 1 - r, c
        else:
            return n - 1 - r, n - 1 - c
