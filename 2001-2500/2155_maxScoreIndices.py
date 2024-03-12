class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        zero = [0] * (len(nums) + 1)
        one = [0] * (len(nums) + 1)

        for i in range(1, len(nums) + 1):
            zero[i] = zero[i - 1] + int(nums[i - 1] == 0)
            
        for i in range(len(nums) - 1, -1, -1):
            one[i] = one[i + 1] + int(nums[i] == 1)

        for i in range(len(nums)):
            zero[i] += one[i]
        
        max_indices = defaultdict(list)

        for i, num in enumerate(zero):
            max_indices[num].append(i)
        
        return max_indices[max(max_indices.keys())]
