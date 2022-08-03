class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        pairs = set()
        i = 0
        j = 1
        while j < len(nums):
            if nums[j] - nums[i] < k:
                j += 1
            elif nums[j] - nums[i] > k:
                i += 1
            elif nums[j] - nums[i] == k:
                if (nums[i], nums[j]) not in pairs:
                    count += 1
                    pairs.add((nums[i], nums[j]))
                i += 1
                j += 1
            if i == j:
                j += 1
        return count
