class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        stack, maximum, current = -1, 0, 0
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                if stack == -1:
                    current = 1
                    maximum = max(maximum, current)
                else:
                    if stack == 0:
                        current += 1
                        maximum = max(maximum, current)
                    else:
                        current = 1
                stack = 1
            elif arr[i] < arr[i - 1]:
                if stack == -1:
                    current = 1
                    maximum = max(maximum, current)
                else:
                    if stack == 1:
                        current += 1
                        maximum = max(maximum, current)
                    else:
                        current = 1
                stack = 0
            else:
                current = 0
                stack = -1
        return maximum + 1
