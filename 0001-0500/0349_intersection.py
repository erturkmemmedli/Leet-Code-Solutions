class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        list1 = list(set1)
        list2 = list(set2)
        output = []
        for item in list1:
            if item in set2: output.append(item)
        return output
      
# Alternative solution

class Solution1:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        output = set()
        for item in nums2:
            if item in set1: output.add(item)
        return output
