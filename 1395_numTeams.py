from collections import defaultdict

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        count = 0
        greater = defaultdict(int)
        less = defaultdict(int)
        for i in range(n-1):
            for j in range(i+1, n):
                if rating[i] < rating[j]:
                    greater[i] += 1
                else:
                    less[i] += 1
        for i in range(n-2):
            for j in range(i+1, n-1):
                if rating[i] < rating[j]:
                    count += greater[j]
                else:
                    count += less[j]
        return count
