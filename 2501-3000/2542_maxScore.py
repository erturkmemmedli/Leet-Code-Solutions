class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [(x, y) for x, y in zip(nums1, nums2)]
        pairs.sort(key = lambda x: -x[1])
        heap = []
        total = 0

        for i in range(k):
            heappush(heap, pairs[i][0])
            total += pairs[i][0]
        
        max_product = total * pairs[k-1][1]

        for i in range(k, len(nums1)):
            pop = heappop(heap)
            heappush(heap, pairs[i][0])
            total += pairs[i][0] - pop
            max_product = max(max_product, total * pairs[i][1])

        return max_product

# Alternative solution (which gives TLE error)

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        self.result = 0
        self.dfs(nums1, nums2, 0, 0, inf, k)
        return self.result

    def dfs(self, nums1, nums2, length, total, minimum, k):
        if length == k:
            self.result = max(self.result, total * minimum)
            return

        for i in range(len(nums1)):
            self.dfs(nums1[i+1:], nums2[i+1:], length + 1, total + nums1[i], min(minimum, nums2[i]), k)
