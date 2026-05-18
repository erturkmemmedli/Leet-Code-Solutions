class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        count = 0
        for i in range(n):
            x = arr[i]
            for j in range(i+1, n):
                y = arr[j]
                for k in range(j+1, n):
                    z = arr[k]
                    if abs(x-y) <= a and abs(y-z) <= b and abs(x-z) <= c:
                        count += 1
        return count
