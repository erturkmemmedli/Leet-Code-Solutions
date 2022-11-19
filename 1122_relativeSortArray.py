from collections import Counter

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr = []
        c = Counter(arr1)
        for num in arr2:
            arr += [num] * c[num]
            del(c[num])
        return arr + sorted(c.elements())
