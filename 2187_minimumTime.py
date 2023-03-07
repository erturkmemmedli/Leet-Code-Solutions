class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        low = 1
        high = min(time) * totalTrips

        while low < high:
            mid = low + (high - low) // 2
            
            if sum(mid // t for t in time) >= totalTrips:
                high = mid
            else:
                low = mid + 1

        return high

# Alternative solution (which gives TLE error)

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        heap = []
        tripCount = 0

        for t in time:
            heappush(heap, (t, t))

        while tripCount < totalTrips:
            position, duration = heappop(heap)
            tripCount += 1
            heappush(heap, (position + duration, duration))

        return position
