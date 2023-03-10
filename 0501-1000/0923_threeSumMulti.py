class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        C = collections.Counter(arr)
        arr = sorted(C.keys())
        n = len(arr)
        result = 0
        for i in range(n):
            x = target - arr[i]
            j, k = i, n - 1
            while j <= k:
                if arr[j] + arr[k] > x:
                    k -= 1
                elif arr[j] + arr[k] < x:
                    j += 1
                else:
                    if arr[i] == arr[j] == arr[k]:
                        result += sum([u * (C[arr[i]] - u - 1) for u in range(1, C[arr[i]] - 1)]) if C[arr[i]] > 1 else 0
                    elif arr[i] == arr[j]:
                        result += (C[arr[i]] - 1) * C[arr[i]] * C[arr[k]] // 2
                    elif arr[j] == arr[k]:
                        result += C[arr[i]] * (C[arr[k]] - 1) * C[arr[k]] // 2
                    else:
                        result += C[arr[i]] * C[arr[j]] * C[arr[k]]
                    k -= 1
                    j += 1
        return result % 1000000007
