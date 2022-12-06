class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        i, j, increasing, decreasing, longest = 0, 1, False, False, 0
        while j < len(arr):
            if arr[j] == arr[j-1]:
                if increasing:
                    increasing = False
                elif decreasing:
                    decreasing = False
                    longest = max(longest, j - i)
                i = j
                j += 1
            elif arr[j] < arr[j-1]:
                if increasing:
                    increasing = False
                    decreasing = True
                elif not decreasing:
                    i = j
                j += 1
            else:
                increasing = True
                if decreasing:
                    longest = max(longest, j - i)
                    i = j - 1
                else:
                    j += 1
                decreasing = False
        if decreasing:
            longest = max(longest, j - i)
        return longest
