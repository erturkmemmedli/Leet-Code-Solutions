class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if len(matchsticks) < 4: return False
        perimeter = sum(matchsticks)
        if perimeter % 4 != 0: return False
        side = perimeter // 4
        matchsticks.sort(reverse = True)
        if matchsticks[0] > side: return False

        @lru_cache
        def dfs(target, s1, s2, s3, s4, index):
            if index == len(matchsticks):
                if s1 == s2 == s3 == s4:
                    return True
            if s1 + matchsticks[index] <= target:
                if dfs(target, s1 + matchsticks[index], s2, s3, s4, index + 1):
                    return True
            if s2 + matchsticks[index] <= target:
                if dfs(target, s1, s2 + matchsticks[index], s3, s4, index + 1):
                    return True
            if s3 + matchsticks[index] <= target:
                if dfs(target, s1, s2, s3 + matchsticks[index], s4, index + 1):
                    return True
            if s4 + matchsticks[index] <= target:
                if dfs(target, s1, s2, s3, s4 + matchsticks[index], index + 1):
                    return True
            return False

        return dfs(side, 0, 0, 0, 0, 0)

# Alternative solution (which does not include cache so gives TLE error)

class Solution1:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if len(matchsticks) < 4: return False
        perimeter = sum(matchsticks)
        if perimeter % 4 != 0: return False
        side = perimeter // 4
        matchsticks.sort(reverse = True)
        if matchsticks[0] > side: return False
        square = [0] * 4
        return self.dfs(matchsticks, side, square, 0)
    
    def dfs(self, matchsticks, target, square, index):
        if index == len(matchsticks):
            if all(square[i] == square[i+1] for i in range(3)):
                return True
        for i in range(4):
            if square[i] + matchsticks[index] <= target:
                square[i] += matchsticks[index]
                if self.dfs(matchsticks, target, square, index + 1):
                    return True
                square[i] -= matchsticks[index]
        return False
