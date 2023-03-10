class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        k = len(arr) // 4
        for i in range(len(arr) - k):
            if arr[i] == arr[i + k]:
                return arr[i]
