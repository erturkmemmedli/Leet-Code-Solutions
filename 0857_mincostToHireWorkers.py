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
