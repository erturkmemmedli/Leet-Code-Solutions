class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        points = []
        for start, end in intervals:
            points.append((start, 1))
            points.append((end, 0))
        points.sort(key = lambda x: [x[0], x[1]])
        roomRequired = 0
        currentRoom = 0
        for point, isStart in points:
            if isStart:
                currentRoom += 1
            else:
                currentRoom -= 1
            roomRequired = max(roomRequired, currentRoom)
        return roomRequired

# Alternative solution

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: [x[0], -x[1]])
        heap = [intervals[0][1]]

        for i in range(1, len(intervals)):
            l, r = intervals[i]

            if l >= heap[0]:
                heappop(heap)
            
            heappush(heap, r)

        return len(heap)
