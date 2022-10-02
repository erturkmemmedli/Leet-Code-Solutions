class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        locations = [0] * 1001
        for num, fr, to in trips:
            if num > capacity: return False
            locations[fr] += num
            locations[to] -= num
        for i in range(1, len(locations)):
            locations[i] += locations[i-1]
            if locations[i] > capacity: return False
        return True
