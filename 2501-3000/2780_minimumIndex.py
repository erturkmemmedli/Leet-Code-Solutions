class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        dominant_element, dominant_count = Counter(nums).most_common()[0]
        n = len(nums)
        current = 0

        for i in range(len(nums)):
            if nums[i] == dominant_element:
                current += 1

            if i + 1 < current * 2 and n - i - 1 < (dominant_count - current) * 2:
                return i

        return -1
