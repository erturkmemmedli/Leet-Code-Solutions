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

# Alternative solution

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        stack = [float('inf') for _ in range(len(nums) + 1)]
        deck = [[] for _ in range(len(nums) + 1)]
        path = [[0] for _ in range(len(nums) + 1)]

        for num in nums:
            idx = bisect_left(stack, num)
            num_path = 1

            if idx > 0:
                i = bisect_right(deck[idx - 1], -num)
                num_path = path[idx - 1][-1] - path[idx - 1][i]

            stack[idx] = num
            deck[idx].append(-num)
            path[idx].append(num_path + path[idx][-1])

        return path[path.index([0]) - 1][-1]
