class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        boardMap = {char : ((ord(char) - 97) // 5, (ord(char) - 97) % 5) for char in string.ascii_lowercase}
        command = ""
        x, y = 0, 0
        for char in target:
            if char != 'z':
                if x == 5 and y == 0:
                    command += 'U'
                    x, y = 4, 0
                tx, ty = boardMap[char]
                dx, dy = tx - x, ty - y
                if dx == 0 and dy == 0:
                    command += '!'
                elif dx >= 0 and dy >= 0:
                    command += dy * 'R' + dx * 'D' + '!'
                elif dx >= 0 and dy <= 0:
                    command += -dy * 'L' + dx * 'D' + '!'
                elif dx <= 0 and dy >= 0:
                    command += dy * 'R' + -dx * 'U' + '!'
                elif dx <= 0 and dy <= 0:
                    command += -dy * 'L' + -dx * 'U' + '!'
                x, y = tx, ty
            else:
                command += y * 'L' + (5 - x) * 'D' + '!'
                x, y = 5, 0
        return command
