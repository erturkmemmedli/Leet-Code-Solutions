class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        l_row = [king[0], -1]
        r_row = [king[0], 8]
        u_col = [-1, king[1]]
        d_col = [8, king[1]]
        l_u_diag = [-1, -1]
        r_u_diag = [-1, 8]
        l_d_diag = [8, -1]
        r_d_diag = [8, 8]
        for queen in queens:
            if queen[0] == king[0]: # looks at row
                if queen[1] < king[1] and queen[1] > l_row[1]: # for left row
                    l_row = queen
                if queen[1] > king[1] and queen[1] < r_row[1]: # for right row
                    r_row = queen
            elif queen[1] == king[1]: # looks at columnn
                if queen[0] < king[0] and queen[0] > u_col[0]: # for upper column
                    u_col = queen
                if queen[0] > king[0] and queen[0] < d_col[0]: # for down column
                    d_col = queen
            elif king[0] - queen[0] == king[1] - queen[1]: # for diagonal
                if queen[0] < king[0] and queen[0] > l_u_diag[0]: # for upper left part of diagonal
                    l_u_diag = queen
                if queen[0] > king[0] and queen[0] < r_d_diag[0]: # for down right part of diagonal
                    r_d_diag = queen
            elif king[0] - queen[0] == queen[1] - king[1]: # for inverse diagonal
                if queen[0] < king[0] and queen[0] > r_u_diag[0]: # for down left part of inverse diagonal
                    r_u_diag = queen
                if queen[0] > king[0] and queen[0] < l_d_diag[0]: # for down right part of inverse diagonal
                    l_d_diag = queen
        output = []
        for a, b in l_row, r_row, u_col, d_col, l_u_diag, r_u_diag, l_d_diag, r_d_diag:
            if 0 <= a < 8 and 0 <= b < 8:
                output.append([a, b])
        return output
