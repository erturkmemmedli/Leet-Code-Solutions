class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        presum = [0]
        for num in nums:
            presum.append(num + presum[-1])
        preset = collections.defaultdict(int)
        count = 0
        for num in presum:
            if num - k in preset:
                count += preset[num - k]
            preset[num] += 1
        return count
