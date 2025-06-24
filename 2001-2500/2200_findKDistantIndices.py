class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        indices = [i for i in range(n) if nums[i] == key]
        result = []

        for i in indices:
            if not result:
                for j in range(max(0, i-k), min(n, i+k+1)):
                    result.append(j)
            elif result[-1] < i+k:
                for j in range(max(result[-1]+1, i-k), min(n, i+k+1)):
                    result.append(j)

        return result
