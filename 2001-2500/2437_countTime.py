class Solution:
    def countTime(self, time: str) -> int:
        answer = 1
        if time[0] == '0' or time[0] == '1':
            if time[1] == '?':
                answer *= 10
            if time[3] == '?':
                answer *= 6
            if time[4] == '?':
                answer *= 10
            return answer
        if time[0] == '2':
            if time[1] == '?':
                answer *= 4
            if time[3] == '?':
                answer *= 6
            if time[4] == '?':
                answer *= 10
        if time[0] == '?':
            if time[1] == '?':
                answer = 24
            elif time[1] not in '0123':
                answer = 2
            else:
                answer = 3
            if time[3] == '?':
                answer *= 6
            if time[4] == '?':
                answer *= 10
        return answer

# Alternative solution

class Solution:
    def countTime(self, time: str) -> int:
        hour, minute = time.split(':')

        hour_front = hour[0]
        hour_end = hour[1]
        minute_front = minute[0]
        minute_end = minute[1]

        if minute_front != '?' and minute_front in ['6', '7', '8', '9']:
            return 0
        if hour_front != '?' and hour_front not in ['0', '1', '2']:
            return 0
        if hour_front == '2' and hour_end not in ['?', '0', '1', '2', '3']:
            return 0
        
        count = 1

        if hour_front == '?':
            if hour_end == '?':
                count *= 24
            elif hour_end in ['0', '1', '2', '3']:
                count *= 3
            else:
                count *= 2
        
        if hour_end == '?':
            if hour_front in ['0', '1']:
                count *= 10
            elif hour_front == '2':
                count *= 4

        if minute_front == '?':
            count *= 6

        if minute_end == '?':
            count *= 10

        return count
