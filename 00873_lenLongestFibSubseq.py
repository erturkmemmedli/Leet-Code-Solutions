class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        hashset = set(arr)
        maximum = max(arr)
        length = 0
        for i in range(1, len(arr)):
            for j in range(i):
                if arr[i] + arr[j] not in hashset:
                    continue
                prev, curr = arr[i], arr[i] + arr[j]
                temp = 3
                while curr <= maximum:
                    prev, curr = curr, curr + prev
                    if curr not in hashset:
                        break
                    else:
                        temp += 1
                length = max(length, temp)
        return length
