class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        total = 0
        for i in range(len(arr)):
            while stack and arr[i] <= arr[stack[-1]]:
                mid = stack.pop()
                prev = stack[-1] if stack else -1
                next = i
                total += arr[mid] * (mid - prev) * (next - mid)
            stack.append(i)
        next = len(arr)
        while stack:
                mid = stack.pop()
                prev = stack[-1] if stack else -1
                total += arr[mid] * (mid - prev) * (next - mid)
        return total % 1_000_000_007
