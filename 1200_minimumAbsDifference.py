class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        diff = float('inf')
        for i in range(1, len(arr)):
            diff = min(arr[i] - arr[i-1], diff)
        result = []
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] == diff:
                result.append([arr[i-1], arr[i]])
        return result
