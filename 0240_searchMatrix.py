class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        self.flag = False
        row = self.binary_search_row(matrix, 0, m - 1, target)
        if self.flag: return True
        if row == -1: return False
        for i in range(row + 1):
            if matrix[i][-1] < target:
                continue
            elif matrix[i][-1] == target:
                return True
            else:
                if self.binary_search_column(matrix[i], 0, n-1, target):
                    return True
        return False
    
    def binary_search_row(self, matrix, left, right, target):
        if left == right:
            if matrix[left][0] > target:
                return left - 1
            else:
                return left
        if left > right:
            return right
        mid = (left + right) // 2
        if matrix[mid][0] == target:
            self.flag = True
            return mid
        elif matrix[mid][0] < target:
            return self.binary_search_row(matrix, mid + 1, right, target)
        else:
            return self.binary_search_row(matrix, left, mid - 1, target)

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
