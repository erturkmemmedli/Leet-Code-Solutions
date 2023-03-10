class Solution:
    def __init__(self):
        self.win = {1:[[0,0],[0,1],[0,2]],
                    2:[[1,0],[1,1],[1,2]],
                    3:[[2,0],[2,1],[2,2]],
                    4:[[0,0],[1,0],[2,0]],
                    5:[[0,1],[1,1],[2,1]],
                    6:[[0,2],[1,2],[2,2]],
                    7:[[0,0],[1,1],[2,2]],
                    8:[[2,0],[1,1],[0,2]]}
    
    def tictactoe(self, moves: List[List[int]]) -> str:
        A = []
        B = []
        for i in range(len(moves)):
            if i % 2 == 0:
                A.append(moves[i])
            else:
                B.append(moves[i])
        for v in self.win.values():
            if v[0] in A and v[1] in A and v[2] in A:
                return "A"
            if v[0] in B and v[1] in B and v[2] in B:
                return "B"
        if len(moves) == 9:
            return "Draw"
        return "Pending"
