class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n, m, count = len(strs), len(strs[0]), 0
        checkList = set(range(n-1))
        for j in range(m):
            if any(strs[i][j] > strs[i+1][j] for i in checkList):
                count += 1
            else:
                checkList -= {i for i in checkList if strs[i][j] < strs[i+1][j]}
        return count
