class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        apple_sum = sum(apple)
        capacity.sort(reverse=True)
        total = 0

        for i in range(len(capacity)):
            apple_sum -= capacity[i]
            total += 1
            if apple_sum <= 0:
                break

        return total
