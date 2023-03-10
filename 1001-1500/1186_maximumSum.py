class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        if len(arr) == 1: return arr[0]
        maximum = nodelete = delete = -float('inf')
        for a in arr:
            delete = max(nodelete, delete + a)
            nodelete = max(a, nodelete + a)
            maximum = max(maximum, nodelete, delete)
        return maximum

# Alternative solution

class Solution1:
    def maximumSum(self, arr: List[int]) -> int:
        if len(arr) == 1: return arr[0]
        maximum = self.KadaneAlgorithm(arr, -1)
        for i in range(len(arr)):
            maximum = max(maximum, self.KadaneAlgorithm(arr, i))
        return maximum

    def KadaneAlgorithm(self, arr, idx):
        curMax, maxSum = 0, -float('inf')
        for i in range(len(arr)):
            if i == idx: continue
            curMax = max(curMax + arr[i], arr[i])
            maxSum = max(maxSum, curMax)
        return maxSum
