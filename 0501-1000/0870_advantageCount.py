class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        heap1, heap2 = [], []
        for i in range(len(nums1)):
            heapq.heappush(heap1, (-nums1[i], i))
            heapq.heappush(heap2, (-nums2[i], i))
        pairs = []
        temp = []
        while heap1 and heap2:
            p1, i1 = heapq.heappop(heap1)
            p2 = -math.inf
            while heap2 and p2 <= p1:
                p2, i2 = heapq.heappop(heap2)
                if p2 <= p1:
                    temp.append(i2)
            if i1 != i2:
                pairs.append((i1, i2))
        while heap1:
            p1, i1 = heapq.heappop(heap1)
            i2 = temp.pop()
            if i1 != i2:
                pairs.append((i1, i2))
        newNums1 = nums1[:]
        for a, b in pairs:
            newNums1[b] = nums1[a]
        return newNums1
