class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        dp = [[0] * 26]
        for i, char in enumerate(s):
            dp.append(dp[i][:])
            dp[i+1][ord(char) - ord('a')] += 1
        return [sum((dp[right+1][i] - dp[left][i]) % 2 for i in range(26)) // 2 <= k for left, right, k in queries] 

# Alternative solution (which gives TLE error)

class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        output = []
        for left, right, k in queries:
            substring = s[left:right+1]
            counter = collections.Counter(substring)
            odd = sum([val % 2 == 1 for val in counter.values()])
            output.append(True if odd - 1 <= k * 2 else False)
        return output
