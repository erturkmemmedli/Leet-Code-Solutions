class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
            
        memo = {}
        
        def dp(i, j, k):
            if k == len(s3):
                return True

            if (i, j) in memo:
                return memo[(i, j)]

            if i < len(s1) and j < len(s2) and s1[i] == s3[k] and s2[j] == s3[k]:
                memo[(i, j)] = dp(i + 1, j, k + 1) or dp(i, j + 1, k + 1)

            elif i < len(s1) and s1[i] == s3[k]:
                memo[(i, j)] = dp(i + 1, j, k + 1)

            elif j < len(s2) and s2[j] == s3[k]:
                memo[(i, j)] = dp(i, j + 1, k + 1)

            else:
                return False

            return memo[(i, j)]

        return dp(0, 0, 0)
