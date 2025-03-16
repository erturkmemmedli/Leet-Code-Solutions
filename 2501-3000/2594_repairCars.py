class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l = 1
        r = max(ranks) * (cars ** 2)
        answer = r

        while l <= r:
            mid = (l + r) // 2

            if sum(int(sqrt(mid // rank)) for rank in ranks) < cars:
                l = mid + 1
            else:
                r = mid - 1
                answer = mid

        return answer
