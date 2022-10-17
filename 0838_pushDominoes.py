class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        result = ""
        i = 0
        right = -1
        while i < len(dominoes):
            if dominoes[i] == 'L':
                if right == -1:
                    result += 'L' * (i + 1 - len(result))
                else:
                    distance = i - right + 1
                    if distance % 2 == 1:
                        result += 'R' * (distance // 2) + '.' + 'L' * (distance // 2)
                    else:
                        result += 'R' * (distance // 2) + 'L' * (distance // 2)
                right = -1
            if dominoes[i] == 'R':
                if right == -1:
                    result += '.' * (i - len(result))
                    right = i
                else:
                    result += 'R' * (i - right)
                    right = i
            i += 1
        if right != -1:
            result += 'R' * (len(dominoes) - len(result))
        else:
            result += '.' * (len(dominoes) - len(result))
        return result
