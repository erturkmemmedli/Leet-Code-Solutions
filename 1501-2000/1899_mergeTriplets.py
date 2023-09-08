class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a, b, c = target
        first = second = third = 0

        for x, y, z in triplets:
            if x <= a and y <= b and z <= c:
                first = max(first, x)
                second = max(second, y)
                third = max(third, z)

        return first == a and second == b and third == c
