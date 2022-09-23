class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        count = 0
        i = 0
        determine = arr[0]
        while i < len(arr):
            determine = max(determine, arr[i])
            if i == determine:
                count += 1
            i += 1
        return count
