class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        n = len(persons)
        candidates = collections.defaultdict(int)
        self.winner = []
        maximum = 0
        winner = -1
        for i in range(n):
            candidates[persons[i]] += 1
            if candidates[persons[i]] >= maximum:
                maximum = candidates[persons[i]]
                winner = persons[i]
            self.winner.append(winner)

    def q(self, t: int) -> int:
        time = bisect.bisect_right(self.times, t)
        return self.winner[time - 1]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
