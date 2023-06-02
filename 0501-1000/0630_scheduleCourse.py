class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key = lambda x: x[1])
        heap = []
        current_time = 0

        for duration, end_time in courses:
            current_time += duration
            heappush(heap, -current_time)

            if current_time > end_time:
                current_time += heappop(heap)

        return len(heap)
