class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        balance = 0
        start = 0
        result = []
        for i in range(len(s)):
            if s[i] == '1':
                balance += 1
            else:
                balance -= 1
            if balance == 0:
                result.append('1' + self.makeLargestSpecial(s[start + 1: i]) + '0')
                start = i + 1
        result = sorted(result, reverse = True)
        return "".join(result)
