class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        prefixSum = collections.deque([shifts[-1]])
        for i in range(len(shifts)-2, -1, -1):
            prefixSum.appendleft((prefixSum[0] + shifts[i]) % 26)
        result = ""
        for i, char in enumerate(s):
            order = (ord(char) - 97 + prefixSum[i]) % 26
            result += chr(97 + order)
        return result
