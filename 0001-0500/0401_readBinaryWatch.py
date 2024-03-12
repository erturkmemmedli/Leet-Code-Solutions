class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn == 0:
            return ['0:00']

        hours = [1, 2, 4, 8]
        minutes = [1, 2, 4, 8, 16, 32]
        result = set()

        def dfs(hours, minutes, time, h, m):
            if h > 11 or m > 59 or time < 0:
                return
            if time == 0:
                result.add(str(h) + ':' + (str(m) if m > 9 else '0' + str(m)))
                return
                
            for i in range(len(hours)):
                dfs(hours[:i] + hours[i+1:], minutes, time - 1, h + hours[i], m)
            
            for i in range(len(minutes)):
                dfs(hours, minutes[:i] + minutes[i+1:], time - 1, h, m + minutes[i])

        dfs(hours, minutes, turnedOn, 0, 0)
        return result
