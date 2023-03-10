from collections import Counter, defaultdict

class Solution:
    def numSplits(self, s: str) -> int:
        store = Counter(s)
        temp = defaultdict(int)
        count = 0
        for char in s:
            store[char] -= 1
            temp[char] += 1
            if store[char] == 0: del(store[char])
            if len(store) == len(temp): count += 1
        return count
