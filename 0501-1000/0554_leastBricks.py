class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        dp = collections.defaultdict(int)
        for row in wall:
            for i in range(len(row) - 1):
                if i == 0:
                    index = row[i]
                else:
                    index += row[i]
                dp[index] += 1
        return len(wall) - max(dp.values()) if dp else len(wall)
