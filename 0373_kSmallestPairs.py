class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        def insert(i, j):
            if i < len(nums1) and j < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j], i, j))
        insert(0, 0)
        kPairs = []
        while k and heap:
            summ, x, y = heapq.heappop(heap)
            kPairs.append([nums1[x], nums2[y]])
            insert(x, y + 1)
            if y == 0: insert(x + 1, y)
            k -= 1
        return kPairs

# Alternative solution (which gives MLE error)

class Solution1:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        for i in nums1:
            for j in nums2:
                heapq.heappush(heap, (i + j, i, j))
        result = []
        for _ in range(k):
            if heap:
                summ, x, y = heapq.heappop(heap)
                result.append([x, y])
            else:
                break
        return result
        
# Alternative solution (which gives TLE error)

class Solution2:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        return heapq.nsmallest(k, ((a, b) for a in nums1 for b in nums2), key = sum)
