class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        result, current = set(), set()
        for num in arr:
            current = {num} | {num | val for val in current}
            result |= current
        return len(result)

# Alternative solution (which gives TLE error)

class Solution1:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        result = set(arr)
        dp = arr.copy()
        while len(dp) > 1:
            temp = []
            for i in range(len(dp) - 1):
                bitwiseOR = arr[i] | dp[i+1]
                result.add(bitwiseOR)
                temp.append(bitwiseOR)
            dp = temp
        return len(result)
