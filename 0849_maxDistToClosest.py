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
