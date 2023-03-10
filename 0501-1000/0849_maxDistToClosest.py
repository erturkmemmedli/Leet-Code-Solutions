class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        distance = 0
        first_seat = True
        i = 0
        for idx, seat in enumerate(seats):
            if seat:
                if first_seat:
                    distance = max(distance, idx)
                    i = idx
                    first_seat = False
                else:
                    distance = max(distance, (idx+i)//2 - i)
                    i = idx
            if idx == len(seats) - 1:
                distance = max(distance, idx - i)
        return distance

# Alternative solution

class Solution1:
    def maxDistToClosest(self, seats: List[int]) -> int:
        occupiedSeats = []
        for i, seat in enumerate(seats):
            if seat == 1:
                occupiedSeats.append(i)
        maxDistance = occupiedSeats[0]
        for i in range(len(occupiedSeats) - 1):
            distance = occupiedSeats[i+1] - occupiedSeats[i]
            maxDistance = max(maxDistance, distance // 2)
        maxDistance = max(maxDistance, len(seats) - occupiedSeats[-1] - 1)
        return maxDistance
