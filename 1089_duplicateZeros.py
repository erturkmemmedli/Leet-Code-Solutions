class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        d = {}
        count = 0
        for idx, num in enumerate(arr):
            if num == 0:
                count += 1
                continue
            if idx + count < len(arr):
                d[idx + count] = num
            else:
                break
        for i in range(len(arr)):
            arr[i] = d.get(i, 0)
