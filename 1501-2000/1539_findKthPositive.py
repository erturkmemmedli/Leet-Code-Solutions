class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        last = 0
        length = len(arr)
        left, right = 0, length - 1
        missing = 0
        while left <= right:
            mid = left + (right - left) // 2
            count = mid - left + 1
            elements = arr[mid] - last - count
            if missing + elements < k:
                missing += elements
                last = arr[mid]
                left = mid + 1
            else:
                right = mid - 1
        return last + k - missing
