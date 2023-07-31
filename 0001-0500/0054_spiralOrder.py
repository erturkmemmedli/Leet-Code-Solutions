class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        x, y, dx, dy = 0, 0, 0, 1
        spiral = []
        while len(spiral) < m * n:
            spiral.append(matrix[x][y])
            matrix[x][y] = None
            if 0 <= x + dx < m and 0 <= y + dy < n and matrix[x + dx][y + dy] != None:
                x += dx
                y += dy
            else:
                dx, dy = dy, -dx
                x += dx
                y += dy
        return spiral

# Alternative solution

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        left_edge, right_edge, top_edge, bottom_edge = 0, n - 1, 0, m - 1
        right, left, down, up = True, False, False, False
        output = [matrix[0][0]]
        row, col = 0, 0

        while right or left or down or up:
            top_edge += 1
            while right:
                if col + 1 <= right_edge:
                    col += 1
                    output.append(matrix[row][col])
                else:
                    right = False
                    if row + 1 <= bottom_edge:
                        down = True
                        
            right_edge -= 1
            while down:
                if row + 1 <= bottom_edge:
                    row += 1
                    output.append(matrix[row][col])
                else:
                    down = False
                    if col - 1 >= left_edge:
                        left = True         

            bottom_edge -= 1
            while left:
                if col - 1 >= left_edge:
                    col -= 1
                    output.append(matrix[row][col])
                else:
                    left = False
                    if row - 1 >= top_edge:
                        up = True
                        
            left_edge += 1
            while up:
                if row - 1 >= top_edge:
                    row -= 1
                    output.append(matrix[row][col])
                else:
                    up = False
                    if col + 1 <= right_edge:
                        right = True     

        return output
