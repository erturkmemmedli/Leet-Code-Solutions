class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        self.isThereNeedToContinue = False
        self.numberOfFleets = 0
        pairs = sorted([(i, j) for i, j in zip(position, speed)], reverse = True)
        stack = []
        for position, velocity in pairs:
            time = (target - position) / velocity
            if not stack:
                stack.append(time)
                continue
            if time > stack[-1]:
                stack.append(time)
        return len(stack)
