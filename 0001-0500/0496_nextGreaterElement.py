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

# Alternative solution

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        stack = []
        next_greater = {}
        i = n - 1
        
        while i >= 0:
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
                
            next_greater[nums2[i]] = stack[-1] if stack else -1
            
            stack.append(nums2[i])
            i -= 1
            
        return [next_greater[i] for i in nums1]
