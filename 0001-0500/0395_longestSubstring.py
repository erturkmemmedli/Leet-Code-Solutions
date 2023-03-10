class Solution:
    def __init__(self):
        self.answer = 0
    
    def longestSubstring(self, s: str, k: int) -> int:
        if k > len(s):
            return 0
        self.hashmap = collections.defaultdict(list)
        for i, char in enumerate(s):
            self.hashmap[char].append(i)
        problematicIndexes = collections.deque()
        for key, val in self.hashmap.items():
            if len(val) < k:
                problematicIndexes += deque(val)
        if problematicIndexes:
            problematicIndexes.appendleft(-1)
            problematicIndexes.append(len(s))
        else:
            return len(s)
        for i in range(1, len(problematicIndexes)):
            if problematicIndexes[i] - problematicIndexes[i-1] - 1 >= k:
                self.answer = max(self.answer, self.longestSubstring(s[problematicIndexes[i-1]+1:problematicIndexes[i]], k))
        return self.answer
