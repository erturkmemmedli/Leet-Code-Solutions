class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        start = 1
        end = sum(candies) // k
        answer = 0

        while start <= end:
            mid = start + (end - start) // 2
            if self.splittable(candies, mid, k):
                start = mid + 1
                answer = mid
            else:
                end = mid - 1
            
        return answer


    def splittable(self, candies, mid, k):
        split = 0

        for candy in candies:
            split += candy // mid
        
        return split >= k
