class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        ranks = {char: [0] * len(votes[0]) + [char] for char in votes[0]}
        for vote in votes:
            for i, char in enumerate(vote):
                ranks[char][i] -= 1
        return "".join(sorted(ranks, key = ranks.get))
        
# Alternative solution

class Solution1:
    def rankTeams(self, votes: List[str]) -> str:
        ranks = collections.defaultdict(lambda: [0] * 26)
        for vote in votes:
            for i, char in enumerate(vote):
                ranks[char][i] -= 1
        ranks = sorted(ranks.items(), key = lambda x: [x[1], x[0]])
        return "".join(key for key, val in ranks)
