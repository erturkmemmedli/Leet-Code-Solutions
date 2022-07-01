class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: x[1], reverse = True)
        i = 0
        total = 0
        while truckSize and i < len(boxTypes):
            if boxTypes[i][0] > truckSize:
                total += truckSize * boxTypes[i][1]
                break
            total += boxTypes[i][0] * boxTypes[i][1]
            truckSize -= boxTypes[i][0]
            i += 1
        return total
