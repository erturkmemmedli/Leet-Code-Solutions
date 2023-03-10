class Solution:
    def checkRecord(self, s: str) -> bool:
        absence = 0
        for i in range(len(s)):
            if s[i] == 'A':
                absence += 1
            if s[i] == 'L' and i < len(s) - 2 and s[i:i+3] == 'LLL':
                return False
        return absence < 2
