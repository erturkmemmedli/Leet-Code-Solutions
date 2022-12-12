class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        hashmap = collections.defaultdict(list)
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                if arr[i] * arr[j] <= arr[-1]:
                    hashmap[arr[i] * arr[j]].append((arr[i], arr[j]))
        dp = {num: 1 for num in arr}
        for num in arr:
            for a, b in hashmap[num]:
                if a == b:
                    dp[num] += dp[a] * dp[b]
                else:
                    dp[num] += dp[a] * dp[b] * 2
        return sum(dp.values()) % 1000000007
