from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        C = Counter(s)
        C = sorted(C.items(), key = lambda x: x[1], reverse = True)
        output = ''
        for k, v in C:
            output += k * v
        return output
        
# Alternative solution

from collections import Counter

class Solution1:
    def frequencySort(self, s: str) -> str:
        C = Counter(s)
        output = ""
        for k, v in C.most_common():
            output += k * v
        return output

# Alternative solution

class Solution2:
    def frequencySort(self, s: str) -> str:
        return "".join([key * val for key, val in collections.Counter(s).most_common()])

# Alternative solution

from heapq import heappush, heappop

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        heap = []
        for k, v in freq.items():
            heappush(heap, (-v, k))
        sortedString = ""
        for _ in range(len(heap)):
            count, char = heappop(heap)
            sortedString += char * (-count)
        return sortedString
