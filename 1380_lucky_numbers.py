class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        matrix2 = list(zip(*matrix))
        minimum = set([min(i) for i in matrix])
        maximum = set([max(i) for i in matrix2])
        result = minimum - (minimum - maximum)
        return list(result)
