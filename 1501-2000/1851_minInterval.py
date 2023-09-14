class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key = lambda x: x[0])
        
        queries = [[num, idx] for idx, num in enumerate(queries)]
        queries.sort(key = lambda x: x[0])

        answer = [None] * len(queries)
        heap = []
        curr = 0

        for i, [query, index] in enumerate(queries):
            if i > 0 and queries[i - 1][0] == query:
                answer[index] = answer[queries[i - 1][1]]
                continue

            while curr < len(intervals) and intervals[curr][0] <= query:
                left, right = intervals[curr]
                heapq.heappush(heap, (right - left + 1, right))
                curr += 1
            
            while heap and heap[0][1] < query:
                heapq.heappop(heap)

            answer[index] = heap[0][0] if heap else -1

        return answer
