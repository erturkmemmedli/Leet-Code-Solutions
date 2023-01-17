class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        self.hashTable = collections.defaultdict(set)
        for row, col in reservedSeats:
            self.hashTable[row].add(col)
        maxFourPersonGroup = (n - len(self.hashTable)) * 2
        for key, val in self.hashTable.items():
            maxFourPersonGroup += self.calculateRow(val)
        return maxFourPersonGroup

    def calculateRow(self, row):
        count = 0
        if 2 not in row and 3 not in row and 4 not in row and 5 not in row:
            count += 1
        if 4 not in row and 5 not in row and 6 not in row and 7 not in row and count == 0:
            return 1
        if 8 not in row and 9 not in row and 6 not in row and 7 not in row:
            count += 1
        return count
