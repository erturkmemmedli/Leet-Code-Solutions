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

# Alternative solution

class Solution1(object):
    def findMedianSortedArrays(self, nums1, nums2):
        merged = nums1 + nums2
        merged.sort()
        if len(merged) % 2 == 1:
            return merged[len(merged) // 2]
        else:
            return (merged[len(merged) // 2 - 1] + merged[len(merged) // 2]) / 2

# Alternative solution

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_length = len(nums1) + len(nums2)
        k = total_length // 2

        if not nums1:
            return nums2[k] if total_length & 1 else (nums2[k-1] + nums2[k]) / 2
        if not nums2:
            return nums1[k] if total_length & 1 else (nums1[k-1] + nums1[k]) / 2

        heap = []
        heappush(heap, (nums1[0], 1, 0))
        heappush(heap, (nums2[0], 2, 0))

        while k:
            val, arr_no, idx = heappop(heap)
            k -= 1

            if arr_no == 1 and idx + 1 < len(nums1):
                heappush(heap, (nums1[idx + 1], arr_no, idx + 1))
            if arr_no == 2 and idx + 1 < len(nums2):
                heappush(heap, (nums2[idx + 1], arr_no, idx + 1))
        
        return heap[0][0] if total_length & 1 else (val + heap[0][0]) / 2

# Alternative solution

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        total = m + n
        mid = total // 2
        even = total % 2 == 0
        count = i = j = 0

        while i < m and j < n:
            if (not even and count == mid) or (even and count == mid - 1):
                break

            if nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
            
            count += 1
        
        if i == m:
            idx = j + mid - count
            return nums2[idx] if not even else (nums2[idx] + nums2[idx - 1]) / 2
        if j == n:
            idx = i + mid - count
            return nums1[idx] if not even else (nums1[idx] + nums1[idx - 1]) / 2
        if not even:
            return min(nums1[i], nums2[j])
        else:
            return sum(sorted(nums1[i:i+2] + nums2[j:j+2])[:2]) / 2
