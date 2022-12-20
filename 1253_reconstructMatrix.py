class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        both = colsum.count(2)
        if sum(colsum) != upper + lower or both > lower or both > upper: return []
        binaryMatrix = [[0 for _ in range(len(colsum))] for _ in range(2)]
        possibleUpper = upper - both
        for i in range(len(colsum)):
            if colsum[i] == 2:
                binaryMatrix[0][i] = 1
                binaryMatrix[1][i] = 1
            elif colsum[i] == 0:
                continue
            elif possibleUpper:
                binaryMatrix[0][i] = 1
                possibleUpper -= 1
            else:
                binaryMatrix[1][i] = 1
        return binaryMatrix
