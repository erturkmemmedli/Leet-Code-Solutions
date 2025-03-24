class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        merged_meetings = [meetings[0]]
        count = merged_meetings[0][0] - 1

        for i in range(1, len(meetings)):
            if meetings[i][0] <= merged_meetings[-1][1]:
                merged_meetings[-1][1] = max(merged_meetings[-1][1], meetings[i][1])
            else:
                merged_meetings.append(meetings[i])
            
        for i in range(1, len(merged_meetings)):
            count += merged_meetings[i][0] - merged_meetings[i - 1][1] - 1

        count += days - merged_meetings[-1][1]
        return count
