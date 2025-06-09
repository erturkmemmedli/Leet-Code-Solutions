class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        frequence = Counter(num * k for num in nums2)
        counter = {}
        max_range = max(nums1) + 1

        for num, count in frequence.items():
            for val in range(num, max_range, num):
                counter[val] = counter.get(val, 0) + count

        return sum(counter[num] for num in nums1 if num in counter)
