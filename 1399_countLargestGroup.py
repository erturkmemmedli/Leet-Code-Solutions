from collections import Counter

class Solution:
    def countLargestGroup(self, n: int) -> int:
        group = Counter()
        for i in range(1, n+1):
            string = str(i)
            val = 0
            for s in string:
                val += int(s)
            group[val] += 1
        maximum = max(group.values())
        return sum(group[val] == maximum for val in group)
