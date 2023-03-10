class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        queue = collections.deque(initialBoxes)
        totalCandies = 0
        unusedBoxes = set()
        while queue:
            box = queue.popleft()
            if status[box] == -1:
                continue
            if status[box] == 0:
                unusedBoxes.add(box)
            for b in containedBoxes[box]:
                queue.append(b)
            for k in keys[box]:
                if status[k] == 0:
                    status[k] = 1
                    if k in unusedBoxes:
                        unusedBoxes.remove(k)
                        queue.append(k)
            if status[box] == 1:
                status[box] = -1
                totalCandies += candies[box]
        return totalCandies
