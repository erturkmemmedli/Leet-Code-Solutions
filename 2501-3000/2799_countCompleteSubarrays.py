class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        counter = Counter(nums)
        distinct = len(counter)
        total = 0

        for i in range(len(nums)):
            curr = {nums[i]}
            if len(curr) == distinct:
                total += 1

            for j in range(i + 1, len(nums)):
                curr.add(nums[j])
                if len(curr) == distinct:
                    total += 1

        return total
