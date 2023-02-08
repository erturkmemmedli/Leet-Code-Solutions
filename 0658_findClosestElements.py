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

# Alternative solution

import heapq

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for i in range(k):
            heapq.heappush(heap, (-abs(arr[i] - x), arr[i]))
        for i in range(k, len(arr)):
            if abs(arr[i] - x) < -heap[0][0] or (abs(arr[i] - x) == -heap[0][0] and arr[i] < heap[0][1]):
                heapq.heappop(heap)
                heapq.heappush(heap, (-abs(arr[i] - x), arr[i]))
        return sorted([element for distance, element in heap])
