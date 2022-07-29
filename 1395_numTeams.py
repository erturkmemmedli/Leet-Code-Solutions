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

# Alternative solution

from sortedcontainers import SortedList
from bisect import bisect_left

class Solution1:
    def numTeams(self, rating: List[int]) -> int:
        right = SortedList(rating)
        left = SortedList()
        count = 0
        for soldier in rating:
            right.remove(soldier)
            low_R, high_R = self.separate(right, soldier)
            low_L, high_L = self.separate(left, soldier)
            left.add(soldier)
            count += low_R * high_L + low_L * high_R        
        return count
    
    def separate(self, liste, soldier):
        low = liste.bisect_left(soldier)
        high = len(liste) - low
        return low, high
