class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        taggedHouses = [False] * (n + 1)
        taggedHouses[1] = True
        dp = [0] * (n + 1)
        dp[1] = nums[0]
        firstTaken = None
        for i in range(1, n):
            if i < n - 1:
                if nums[i] + dp[i - 1] >= dp[i]:
                    taggedHouses[i + 1] = taggedHouses[i - 1]
                    dp[i + 1] = nums[i] + dp[i - 1]
                else:
                    taggedHouses[i + 1] = taggedHouses[i]
                    dp[i + 1] = dp[i]
                if taggedHouses[i + 1] == taggedHouses[i]:
                    firstTaken = taggedHouses[i]
            else:
                if firstTaken == False:
                    return max(nums[i] + dp[i - 1], dp[i])
                elif firstTaken == True:
                    forward = dp[i]
                elif firstTaken == None:
                    if nums[i] + dp[i - 1] >= dp[i]:
                        if taggedHouses[i - 1] == False:
                            return nums[i] + dp[i - 1]
                        else:
                            forward = dp[i]
                    else:
                        if taggedHouses[i] == True:
                            return dp[i]
                        else:
                            forward = dp[i]
        dp = [0] * n
        dp[-2] = nums[-1]
        for j in range(n-2, 0, -1):
            dp[j - 1] = max(dp[j + 1] + nums[j], dp[j])
        backward = dp[0]
        return max(forward, backward)
