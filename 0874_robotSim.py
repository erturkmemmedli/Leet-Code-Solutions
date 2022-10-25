from collections import defaultdict
from bisect import bisect_left

class Solution:
    def robotSim(self, commands: list, obstacles: list) -> int:
        x, y, maxx = 0, 0, 0
        compass = [1, 0, 0, 0] # [North, South, East, West]
        x_direction, y_direction = defaultdict(list), defaultdict(list)
        for a, b in obstacles:
            if a or b:
                x_direction[b].append(a)
                y_direction[a].append(b)
        for command in commands:
            if 1 <= command <= 9:
                if compass[0]:
                    if x in y_direction:
                        obs = sorted(y_direction[x])
                        index = bisect_left(obs, y)
                        if index < len(obs):
                            y = min(y + command, obs[index] - 1)
                        else:
                            y += command
                    else:
                        y += command
                elif compass[1]:
                    if x in y_direction:
                        obs = sorted(y_direction[x])
                        index = bisect_left(obs, y)
                        if index > 0:
                            y = max(y - command, obs[index-1] + 1)
                        else:
                            y -= command
                    else:
                        y -= command
                elif compass[2]:
                    if y in x_direction:
                        obs = sorted(x_direction[y])
                        index = bisect_left(obs, x)
                        if index < len(obs):
                            x = min(x + command, obs[index] - 1)
                        else:
                            x += command
                    else:
                        x += command
                elif compass[3]:
                    if y in x_direction:
                        obs = sorted(x_direction[y])
                        index = bisect_left(obs, x)
                        if index > 0:
                            x = max(x - command, obs[index-1] + 1)
                        else:
                            x -= command
                    else:
                        x -= command
                maxx = max(maxx, x ** 2 + y ** 2)
            elif command == -1:
                if compass[0] or compass[1]:
                    compass = compass[2:] + compass[:2]
                elif compass[2]:
                    compass = [0,1,0,0]
                elif compass[3]:
                    compass = [1,0,0,0]
            elif command == -2:
                if compass[2] or compass[3]:
                    compass = compass[2:] + compass[:2]
                elif compass[0]:
                    compass = [0,0,0,1]
                elif compass[1]:
                    compass = [0,0,1,0]
        return maxx

# Alternative solution

from collections import defaultdict
from bisect import bisect_left

class Solution1:
    def robotSim(self, commands: list, obstacles: list) -> int:
        x, y, maxx = 0, 0, 0
        compass = [1, 0, 0, 0] # [North, South, East, West]
        x_direction, y_direction = defaultdict(list), defaultdict(list)
        for a, b in obstacles:
            if a or b:
                x_direction[b].append(a)
                y_direction[a].append(b)
        for command in commands:
            if 1 <= command <= 9:
                if compass[0]:
                    y = self.calculate(x, y, y_direction, min, command, 0, -1)

                elif compass[1]:
                    y = self.calculate(x, y, y_direction, max, -command, -1, 1)

                elif compass[2]:
                    x = self.calculate(y, x, x_direction, min, command, 0, -1)

                elif compass[3]:
                    x = self.calculate(y, x, x_direction, max, -command, -1, 1)
                maxx = max(maxx, x ** 2 + y ** 2)
            elif command == -1:
                if compass[0] or compass[1]:
                    compass = compass[2:] + compass[:2]
                elif compass[2]:
                    compass = [0,1,0,0]
                elif compass[3]:
                    compass = [1,0,0,0]
            elif command == -2:
                if compass[2] or compass[3]:
                    compass = compass[2:] + compass[:2]
                elif compass[0]:
                    compass = [0,0,0,1]
                elif compass[1]:
                    compass = [0,0,1,0]
        return maxx
    
    def calculate(self, var_1, var_2, direction, operation, factor_1, factor_2, factor_3):
        if var_1 in direction:
            obs = sorted(direction[var_1])
            idx = bisect_left(obs, var_2)
            if operation == min:
                left, right = idx, len(obs)
            else:
                left, right = 0, idx
            if left < right:
                var_2 = operation(var_2 + factor_1, obs[idx + factor_2] + factor_3)
            else:
                var_2 += factor_1
        else:
            var_2 += factor_1
        return var_2

    
# Alternative solution

class Solution2:
    def robotSim(self, commands: list, obstacles: list) -> int:
        x, y, dx, dy, maxx = 0, 0, 0, 1, 0
        obstacles = set(map(tuple, obstacles))
        for command in commands:
            if command == -2:
                dx, dy = -dy, dx
            elif command == -1:
                dx, dy = dy, -dx
            else:
                for i in range(command):
                    if (x+dx, y+dy) in obstacles:
                        break
                    x += dx
                    y += dy
                    maxx = max(maxx, x**2 + y**2)  
        return maxx

# Alternative solution

from collections import defaultdict as D
from sortedcontainers import SortedList as L
from bisect import bisect_left as B

class Solution3:
    def robotSim(self, commands: list, obstacles: list) -> int:
        xObstacles, yObstacles = D(L), D(L)
        for a, b in obstacles:
            xObstacles[a].add(b)
            yObstacles[b].add(a)
        maxDistance = 0
        north, south, east, west = [0, 1], [0, -1], [1, 0], [-1, 0]
        direction = north
        x, y = 0, 0
        for command in commands:
            if command == -2:
                if direction == north: direction = west
                elif direction == south: direction = east
                elif direction == east: direction = north
                elif direction == west: direction = south
                continue
            if command == -1:
                if direction == north: direction = east
                elif direction == south: direction = west
                elif direction == east: direction = south
                elif direction == west: direction = north
                continue
            else:
                print(direction)
                if direction[1] > 0:
                    if not obstacles or x not in xObstacles:
                        y += command
                    else:
                        i = B(xObstacles[x], y)
                        if i <= len(xObstacles[x]) - 1 and xObstacles[x][i] != x:
                            bound = xObstacles[x][i] - 1
                            y = min(y + command, bound)
                        else:
                            y += command
                elif direction[1] < 0:
                    if not obstacles or x not in xObstacles:
                        y -= command
                    else:
                        i = B(xObstacles[x], y)
                        if i > 0:
                            bound = xObstacles[x][i - 1] + 1
                            y = max(y - command, bound)
                        else:
                            y -= command
                elif direction[0] > 0:
                    if not obstacles or y not in yObstacles:
                        x += command
                    else:
                        i = B(yObstacles[y], x)
                        if i <= len(yObstacles[y]) - 1 and yObstacles[y][i] != y:
                            bound = yObstacles[y][i] - 1
                            x = min(x + command, bound)
                        else:
                            x += command
                elif direction[0] < 0:
                    if not obstacles or y not in yObstacles:
                        x -= command
                    else:
                        i = B(yObstacles[y], x)
                        if i > 0:
                            bound = yObstacles[y][i - 1] + 1
                            x = max(x - command, bound)
                        else:
                            x -= command
                maxDistance = max(maxDistance, x ** 2 + y ** 2)
        return maxDistance
