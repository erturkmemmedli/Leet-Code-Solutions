class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        nums1 = [- float('inf')] + nums1 + [float('inf')]
        nums2 = [- float('inf')] + nums2 + [float('inf')]
        length = len(nums1) + len(nums2)
        half = length // 2
        l1 = 0
        r1 = len(nums1) - 1        
        l2 = 0
        r2 = len(nums2) - 1
        m2 = (l2 + r2) // 2                
        while l2 < r2:
            nums2_left = nums2[l2 : m2 + 1]
            nums2_right = nums2[m2 + 1 : r2 + 1]            
            cut = half - m2 - 1                        
            nums1_left = nums1[l1 : cut]
            nums1_right = nums1[cut: r1 + 1]
            if nums2_left[-1] <= nums1_right[0] and nums1_left[-1] <= nums2_right[0]:
                if length % 2 == 0:
                    return (max(nums1_left[-1], nums2_left[-1]) + min(nums1_right[0], nums2_right[0])) / 2
                else:
                    return min(nums1_right[0], nums2_right[0])    
            elif nums2_left[-1] > nums1_right[0]:
                r2 = m2
                m2 = (l2 + r2) // 2                
            elif nums1_left[-1] > nums2_right[0]:
                l2 = m2 + 1
                m2 = (l2 + r2) // 2
