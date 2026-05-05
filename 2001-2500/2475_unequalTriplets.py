class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        c = Counter(nums)
        if len(c) < 3:
            return 0

        key_vals = list(c.items())
        res = 0

        for i in range(0, len(key_vals)):
            for j in range(i + 1, len(key_vals)):
                for k in range(j + 1, len(key_vals)):
                    res += key_vals[i][1] * key_vals[j][1] * key_vals[k][1]

        return res
