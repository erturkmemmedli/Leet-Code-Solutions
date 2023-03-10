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

# Alternative solution

class Solution1:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        hashset = set(arr)
        hashmap = collections.defaultdict(int)
        for i in range(2, len(arr)):
            for j in range(1,i):
                if arr[i] - arr[j] < arr[j] and arr[i] - arr[j] in hashset:
                    hashmap[(arr[i], arr[j])] = hashmap.get((arr[j], arr[i] - arr[j]), 2) + 1
        return max(hashmap.values() or [0])
