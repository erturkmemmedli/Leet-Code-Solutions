class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return [list(map(lambda x: x[i], matrix)) for i in range(len(matrix[0]))]
