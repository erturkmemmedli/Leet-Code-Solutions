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

# Alternative solution

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {0: 1}
        curr_sum = 0
        count = 0

        for num in nums:
            curr_sum += num
            count += hashmap.get(curr_sum - k, 0)
            hashmap[curr_sum] = hashmap.get(curr_sum, 0) + 1

        return count
