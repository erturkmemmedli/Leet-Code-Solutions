class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        swap = [n] * n
        keep = [n] * n
        swap[0] = 1
        keep[0] = 0
        for i in range(1, n):
            both = nums1[i] > nums1[i-1] and nums2[i] > nums2[i-1]
            one = nums1[i] > nums2[i-1] and nums2[i] > nums1[i-1]
            if both:
                swap[i] = swap[i-1] + 1
                keep[i] = keep[i-1]
            if one:
                swap[i] = min(swap[i], keep[i-1] + 1)
                keep[i] = min(keep[i], swap[i-1])
        return min(swap[-1], keep[-1])
