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

# Alternative solution

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        result = []
        heap = []

        for i in range(len(nums1)):
            heappush(heap, (nums1[i] + nums2[0], i, 0))

        while k and heap:
            summ, row, col = heappop(heap)
            result.append([nums1[row], nums2[col]])
            k -= 1

            if col + 1 < len(nums2):
                heappush(heap, (nums1[row] + nums2[col + 1], row, col + 1))
            
        return result

# Alterntive solution

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n = len(nums1)
        m = len(nums2)
        memo = {(0, 0)}
        pairs = []
        heap = [(nums1[0] + nums2[0], 0, 0)]

        while heap:
            s, i1, i2 = heappop(heap)
            pairs.append([nums1[i1], nums2[i2]])
            k -= 1

            if k == 0:
                return pairs

            if (i1 + 1, i2) not in memo and i1 + 1 < n:
                heappush(heap, (nums1[i1 + 1] + nums2[i2], i1 + 1, i2))
                memo.add((i1 + 1, i2))
            if (i1, i2 + 1) not in memo and i2 + 1 < m:
                heappush(heap, (nums1[i1] + nums2[i2 + 1], i1, i2 + 1))
                memo.add((i1, i2 + 1))
            
        return pairs
