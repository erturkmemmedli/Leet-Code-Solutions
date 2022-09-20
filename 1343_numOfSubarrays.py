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
