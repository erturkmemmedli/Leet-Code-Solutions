class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        for i in range(1, len(arr)):
            if arr[i] < arr[i-1]:
                return i-1

# Alternative solution

class Solution1:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid] < arr[mid-1]:
                right = mid
            elif arr[mid] > arr[mid-1]:
                left = mid + 1

# Alternative solution

class Solution:
    def peakIndexInMountainArray(self, arr):
        left, right = 0, len(arr) - 1
        while left + 2 <= right:
            mid = left + (right - left) // 2
            if arr[mid - 1] < arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid + 1] > arr[mid]:
                left = mid
            else:
                right = mid
