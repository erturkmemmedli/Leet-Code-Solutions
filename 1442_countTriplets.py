class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        count = 0
        for i in range(len(arr)-1):
            item = arr[i]
            for j in range(i+1, len(arr)):
                item ^= arr[j]
                if item == 0:
                    count += j - i
        return count
