class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        summ = 0
        count = 0
        i = 0
        while i < len(arr):
            if i < k:
                summ += arr[i]
                i += 1
                if i == len(arr):
                    if summ / k >= threshold:
                        count += 1
                continue
            if summ / k >= threshold:
                count += 1
            summ += arr[i] - arr[i-k]
            i += 1
            if i == len(arr):
                if summ / k >= threshold:
                    count += 1
        return count

# Alternative solution

class Solution:
    def numOfSubarrays(self, arr, k, threshold):
        windowSum = sum(arr[:k])
        count = 1 if windowSum / k >= threshold else 0
        for i in range(len(arr) - k):
            windowSum += arr[i + k] - arr[i]
            if windowSum / k >= threshold:
                count += 1
        return count
