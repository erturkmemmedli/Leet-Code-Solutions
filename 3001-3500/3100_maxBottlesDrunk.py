class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        emptyBottes = 0
        bottlesDrunk = 0

        while numBottles:
            emptyBottes += numBottles
            bottlesDrunk += numBottles
            numBottles = 0

            while emptyBottes >= numExchange:
                emptyBottes -= numExchange
                numExchange += 1
                numBottles += 1

        return bottlesDrunk
