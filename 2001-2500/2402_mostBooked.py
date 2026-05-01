class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key = lambda x: x[0])
        # [[1,27],[11,15],[15,36],[29,49],[41,43],[47,49]]
        booking = []
        available = []
        last_time = defaultdict(int)
        counter = Counter()

        for i in range(n):
            heappush(available, i) 
        i = 0

        while i < len(meetings):
            start, end = meetings[i]
            diff = end - start

            if not available:
                start = max(start, booking[0][0])
            
            while booking and booking[0][0] <= start:
                time, room = heappop(booking)
                heappush(available, room)
            
            if available:
                candidate = heappop(available)
                counter[candidate] += 1
                last_time[candidate] = end if candidate not in last_time or last_time[candidate] < start else last_time[candidate] + diff
                heappush(booking, (last_time[candidate], candidate))

            i += 1
        
        return counter.most_common()[0][0]

# Alternative solution

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        room_counter = defaultdict(int)

        room_heap = []
        meeting_heap = []

        for i in range(n):
            heappush(room_heap, i)

        for start, end in meetings:
            while meeting_heap and meeting_heap[0][0] <= start:
                _, r = heappop(meeting_heap)
                heappush(room_heap, r)

            if room_heap:
                room = heappop(room_heap)
                room_counter[room] += 1
                heappush(meeting_heap, (end, room))
            else:
                m, r = heappop(meeting_heap)
                room_counter[r] += 1
                heappush(meeting_heap, (m + end - start, r))

        max_used = 0
        min_room = n
        
        for k, v in room_counter.items():
            if v > max_used:
                max_used = v
                min_room = k
            elif v == max_used:
                min_room = min(min_room, k)

        return min_room
