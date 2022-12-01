class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        lengthDP, countDP, maxLength = [1] * n, [1] * n, 1
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if lengthDP[i] == lengthDP[j]:
                        lengthDP[i] += 1
                        countDP[i] = countDP[j]
                        maxLength = max(maxLength, lengthDP[i])
                    elif lengthDP[i] == lengthDP[j] + 1:
                        countDP[i] += countDP[j]
        return sum(c for i, c in enumerate(countDP) if lengthDP[i] == maxLength)               
