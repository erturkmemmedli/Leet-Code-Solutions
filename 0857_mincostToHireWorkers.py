class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workerData = sorted([[w/q, q, w] for q, w in zip(quality, wage)])
        heap, sumHeap, minMoney = [], 0, float("inf")
        for ratio, q, w in workerData:
            heapq.heappush(heap, -q)
            sumHeap += q
            if len(heap) > k:
                sumHeap += heapq.heappop(heap)
            if len(heap) == k:
                minMoney = min(minMoney, ratio * sumHeap)
        return minMoney

# Altrnative solution (which gives TLE error)

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        result = float("inf")
        heap = []
        factor = sorted([wage[i]/quality[i] for i in range(len(wage))])
        j = 0

        while j < len(factor):
            for i, (q, w) in enumerate(sorted(zip(quality, wage))):
                if q * factor[j] < w:
                    continue

                heappush(heap, q * factor[j])
                
                if len(heap) == k:
                    result = min(result, sum(heap))
                    heap = []
                    break

            heap = []
            j += 1

        return result
