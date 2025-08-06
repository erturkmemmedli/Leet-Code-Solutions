class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n, m = len(nums1), len(nums2)
        count = 0

        for i in range(n):
            for j in range(m):
                try:
                    div, mod = divmod(nums1[i], nums2[j] * k)
                    if mod == 0:
                        count += 1
                except ZeroDivisionError:
                    pass

        return count
