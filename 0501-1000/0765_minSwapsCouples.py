class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        indexMap = {num: i for i, num in enumerate(row)}
        count = 0
        i = 0
        while i < len(row):
            if row[i] % 2 == 0:
                if row[i+1] != row[i] + 1:
                    x = indexMap[row[i] + 1]
                    indexMap[row[i+1]] = x
                    row[i+1], row[x] = row[x], row[i+1]
                    count += 1
            else:
                if row[i+1] != row[i] - 1:
                    x = indexMap[row[i] - 1]
                    indexMap[row[i+1]] = x
                    row[i+1], row[x] = row[x], row[i+1]
                    count += 1
            i += 2
        return count
