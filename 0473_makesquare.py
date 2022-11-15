class Solution:
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
