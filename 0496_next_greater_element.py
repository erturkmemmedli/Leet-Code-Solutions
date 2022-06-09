class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {nums2[-1] : -1}
        for i in range(len(nums2)-2, -1, -1):
            if nums2[i] < nums2[i+1]:
                d[nums2[i]] = nums2[i+1]
            else:
                temp = nums2[i+1]
                while temp != -1:
                    if nums2[i] >= temp:
                        temp = d[temp]
                    else:
                        d[nums2[i]] = temp
                        break
                d[nums2[i]] = temp   
        return [d[num] for num in nums1]
