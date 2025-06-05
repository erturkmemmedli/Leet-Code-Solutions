class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        num_to_idx_map = defaultdict(int)
        count_map = defaultdict(int)
        output = [0] * len(nums)
        
        for i, num in enumerate(nums):
            num_to_idx_map[num] += i
            count_map[num] += 1

        for i in range(len(nums)):
            output[i] = num_to_idx_map[nums[i]] - count_map[nums[i]] * i
            num_to_idx_map[nums[i]] -= 2*i
            count_map[nums[i]] -= 2

        return output
