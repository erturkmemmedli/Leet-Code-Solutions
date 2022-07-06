class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if destination < start:
            return self.distanceBetweenBusStops(distance, destination, start)
        head = distance[:start]
        mid = distance[start:destination]
        tail = distance[destination:]
        return min(sum(head+tail), sum(mid))
