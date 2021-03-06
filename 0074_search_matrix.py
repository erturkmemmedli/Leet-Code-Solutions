class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        heads = [i[0] for i in matrix]
        left = 0
        right = len(heads) - 1
        mid = (left + right) // 2
        while left < right:
            if target == heads[mid]:
                return True
            if target > heads[mid]:
                if mid + 1 < len(heads) and heads[mid + 1] > target:
                    break
                else:
                    left = mid + 1
                    mid = (left + right) // 2
            if target < heads[mid]:
                if mid - 1 >= 0 and heads[mid - 1] < target:
                    mid -= 1
                    break
                else:
                    right = mid
                    mid = (left + right) // 2
        index = mid
        left = 0
        right = len(matrix[index]) - 1
        mid = (left + right) // 2
        while left <= right:
            mid = (left + right) // 2
            if target == matrix[index][mid]:
                return True
            if target > matrix[index][mid]:
                left = mid + 1
            if target < matrix[index][mid]:
                right = mid - 1
        return False
