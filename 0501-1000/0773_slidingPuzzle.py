class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        queue = deque([(board, 0)])
        visited = set()
        while queue:
            newBoard, step = queue.popleft()
            hashval = self.hashValue(newBoard)
            if hashval == 123450:
                return step
            if hashval not in visited:
                visited.add(hashval)
                for i in range(2):
                    for j in range(3):
                        if newBoard[i][j] == 0:
                            if i - 1 == 0:
                                self.candidateBoard(newBoard, queue, visited, step, i, j, i - 1, j)
                            if i + 1 == 1:
                                self.candidateBoard(newBoard, queue, visited, step, i, j, i + 1, j)
                            if j - 1 >= 0:
                                self.candidateBoard(newBoard, queue, visited, step, i, j, i, j - 1)
                            if j + 1 <= 2:
                                self.candidateBoard(newBoard, queue, visited, step, i, j, i, j + 1)
        return -1

    def candidateBoard(self, board, queue, visited, step, x, y, u, v):
        temp = copy.deepcopy(board)
        temp[x][y], temp[u][v] = temp[u][v], temp[x][y]
        hashval = self.hashValue(temp)
        if hashval not in visited:
            queue.append((temp, step + 1))
            
    def hashValue(self, board):
        hashval = 0
        for i in range(2):
            for j in range(3):
                hashval += board[i][j] * 10 ** (5 - 3 * i - j)
        return hashval
