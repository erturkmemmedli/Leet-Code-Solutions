class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        oddIndices = collections.deque()
        niceSubArrays = 0
        prev = -1
        for i, num in enumerate(nums):
            if num % 2 == 1 and len(oddIndices) < k:
                oddIndices.append(i)
            elif num % 2 == 1:
                idx = oddIndices.popleft()
                if oddIndices:
                    niceSubArrays += (idx - prev) * (i - oddIndices[-1])
                else:
                    niceSubArrays += (idx - prev) * (i - idx)
                prev = idx
                oddIndices.append(i)
        if len(oddIndices) < k:
            return 0
        niceSubArrays += (oddIndices[0] - prev) * (len(nums) - oddIndices[-1])
        return niceSubArrays
