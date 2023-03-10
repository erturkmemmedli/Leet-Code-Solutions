class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = collections.Counter(s)
        heap = []
        maxx = max(counter.values())
        if len(s) % 2 == 1:
            if maxx > len(s) // 2 + 1:
                return ""
        else:
            if maxx > len(s) // 2:
                return ""
        for key, val in counter.items():
            heapq.heappush(heap, (-val, key))
        string = ""
        while heap:
            if len(heap) > 1:
                count1, char1 = heapq.heappop(heap)
                count2, char2 = heapq.heappop(heap)
                string += char1 + char2
                if count1 != -1:
                    heapq.heappush(heap, (count1 + 1, char1))
                if count2 != -1:
                    heapq.heappush(heap, (count2 + 1, char2))
            else:
                string += heapq.heappop(heap)[1]
        return string
