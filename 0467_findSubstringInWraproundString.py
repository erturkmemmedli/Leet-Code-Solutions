class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        dp = collections.defaultdict(list, {p[0] : [1]})
        for i in range(1, len(p)):
            if (26 + ord(p[i]) - ord(p[i-1])) % 26 == 1:
                dp[p[i]].append(min(dp[p[i-1]][-1] + 1, 27))
            else:
                dp[p[i]].append(1)
        result = 0
        for key, val in dp.items():
            m = max(val)
            if m <= 26:
                result += m
            else:
                maximum = 0
                temp = 0
                for i in range(len(val)):
                    if i < len(val)-1 and val[i] != 27 and val[i+1] != 27:
                        temp = 0
                    elif i < len(val)-1 and val[i] != 27 and val[i+1] == 27:
                        temp = val[i]
                    elif val[i] == 27:
                        temp += 26
                    maximum = max(maximum, temp)
                result += maximum
        return result
