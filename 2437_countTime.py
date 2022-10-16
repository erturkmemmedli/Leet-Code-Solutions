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
