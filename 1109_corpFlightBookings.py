class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix = [0] * (n + 1)
        for first, last, seats in bookings:
            prefix[first - 1] += seats
            prefix[last] -= seats
        for i in range(1, n + 1):
            prefix[i] += prefix[i - 1]
        return prefix[:-1]

# Alternative solution (which gives TLE error)

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        bookings.sort(key = lambda x: [x[0], x[1]])
        answer = []
        answer += [0] * (bookings[0][0] - 1)
        for first, last, seat in bookings:
            if not answer or answer[-1] == 0:
                answer += [seat] * (last - first + 1)
            else:
                if first > len(answer):
                    answer += [0] * (first - len(answer) - 1)
                    answer += [seat] * (last - first + 1)
                else:
                    for i in range(first - 1, min(last, len(answer))):
                        answer[i] += seat
                    answer += [seat] * (last - len(answer))
        if len(answer) < n:
            answer += [0] * (n - len(answer))
        return answer
