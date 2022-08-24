class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        List = []
        for arr in matrix:
            List += arr
        List.sort()
        return List[k-1]
      
# Alternative solution

from bisect import bisect_right

class Solution1:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        low = matrix[0][0]
        high = matrix[-1][-1]
        while low < high:
            mid = (low + high) // 2
            if sum(bisect_right(row, mid) for row in matrix) < k:
                low = mid + 1
            else:
                high = mid
        return low
