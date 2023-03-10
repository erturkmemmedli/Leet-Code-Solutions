class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key = lambda x: x[0])
        totalDays = max(end for start, end in events)
        heap = []
        numAttendedEvents = 0
        eventId = 0
        for currentDay in range(1, totalDays + 1):
            while eventId < len(events) and events[eventId][0] == currentDay:
                heapq.heappush(heap, events[eventId][1])
                eventId += 1
            while heap and heap[0] < currentDay:
                heapq.heappop(heap)
            if heap:
                heapq.heappop(heap)
                numAttendedEvents += 1
        return numAttendedEvents
