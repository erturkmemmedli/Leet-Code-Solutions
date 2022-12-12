class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        num = int(math.sqrt(target * 2))
        if num * (num + 1) // 2 < target: num += 1
        determiner = num * (num + 1) // 2 - target
        if determiner % 2 == 0: return num
        num += 1
        determiner = num * (num + 1) // 2 - target
        return num if determiner % 2 == 0 else num + 1
      
# Alternative solution

class Solution1:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        num = int(math.sqrt(target * 2))
        if num * (num + 1) // 2 < target: num += 1
        level = num % 4
        if level == 0: level = 4
        if level in [1, 2]:
            if target % 2 == 1:
                return num
            else:
                return num - level + 3
        else:
            if target % 2 == 0:
                return num
            else:
                return num - level + 5
