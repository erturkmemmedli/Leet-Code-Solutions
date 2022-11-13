class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        idx = bisect.bisect_left(arr, x)
        kClosest = collections.deque()
        if idx < len(arr) and arr[idx] == x:
            kClosest.append(arr[idx])
            k -= 1
            i = idx - 1
            j = idx + 1
        elif 0 < idx < len(arr) and arr[idx] > x:
            i = idx - 1
            j = idx
        elif idx == 0 and arr[idx] > x:
            i = -1
            j = idx
        elif idx == len(arr):
            i = idx - 1
            j = idx
        while k:
            if i >= 0 and j < len(arr):
                if x - arr[i] <= arr[j] - x:
                    kClosest.appendleft(arr[i])
                    i -= 1
                else:
                    kClosest.append(arr[j])
                    j += 1
                k -= 1
            elif i == -1:
                kClosest.append(arr[j])
                j += 1
                k -= 1
            elif j == len(arr):
                kClosest.appendleft(arr[i])
                i -= 1
                k -= 1
        return kClosest
