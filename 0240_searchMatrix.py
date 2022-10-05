class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        self.flag = False
        row = self.binary_search_row(matrix, 0, m - 1, target, 0)
        if self.flag: return True
        row_start = self.binary_search_row(matrix, 0, m - 1, target, -1)
        for i in range(row_start, row + 1):
            if self.binary_search_column(matrix[i], 0, n-1, target):
                return True
        return False
    
    def binary_search_row(self, matrix, left, right, target, ind):
        if left == right:
            if matrix[left][ind] > target:
                return left - 1
            else:
                return left
        if left > right:
            return right
        mid = (left + right) // 2
        if matrix[mid][ind] == target:
            self.flag = True
            return mid
        elif matrix[mid][ind] < target:
            return self.binary_search_row(matrix, mid + 1, right, target, ind)
        else:
            return self.binary_search_row(matrix, left, mid - 1, target, ind)

    def binary_search_column(self, array, left, right, target):
        if left > right:
            return False
        mid = (left + right) // 2
        if array[mid] == target:
            return True
        elif array[mid] < target:
            return self.binary_search_column(array, mid + 1, right, target)
        else:
            return self.binary_search_column(array, left, mid - 1, target)
        
# Alternative solution

class Solution1:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        j = n-1
        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:
                j -= 1
                continue
            if i < m-1:
                if matrix[i+1][j] <= target:
                    i += 1
                else:
                    i += 1
                    j -= 1
            else:
                j -= 1
        return False
