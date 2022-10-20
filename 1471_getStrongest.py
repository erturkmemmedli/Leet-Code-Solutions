class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        sortedArray = sorted(arr)
        median = sortedArray[(len(arr) - 1) // 2]
        kStrongest = []
        i, j = 0, len(arr) - 1
        while k > 0:
            if abs(sortedArray[j] - median) > abs(sortedArray[i] - median):
                kStrongest.append(sortedArray[j])
                j -= 1
            elif abs(sortedArray[j] - median) < abs(sortedArray[i] - median):
                kStrongest.append(sortedArray[i])
                i += 1
            else:
                if sortedArray[i] >= sortedArray[j]:
                    kStrongest.append(sortedArray[i])
                    i += 1
                else:
                    kStrongest.append(sortedArray[j])
                    j -= 1
            k -= 1
        return kStrongest
