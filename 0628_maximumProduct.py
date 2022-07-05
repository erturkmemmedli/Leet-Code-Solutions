class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) > 6:
            nums = nums[:3] + nums[-3:]
        return max([nums[i]*nums[j]*nums[k] for i in range(len(nums)) for j in range(i+1, len(nums)) for k in range(j+1, len(nums))])
      
# Alternative solution

class Solution1:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        if nums[1] >= 0 or nums[-1] < 0:
            return nums[-1] * nums[-2] * nums[-3]
        else:
            if nums[0] * nums[1] > nums[-2] * nums[-3]:
                return nums[0] * nums[1] * nums[-1]
            else:
                return nums[-1] * nums[-2] * nums[-3]
              
# Alternative solution

class Solution2:
    def maximumProduct(self, nums: List[int]) -> int:
        min1, min2, min3, max1, max2, max3 = float('inf'), float('inf'), float('inf'), -float('inf'), -float('inf'), -float('inf')
        for num in nums:
            if num < min1:
                min1, min2, min3 = num, min1, min2
            elif num < min2:
                min2, min3 = num, min2
            elif num < min3:
                min3 = num
            if num > max1:
                max1, max2, max3 = num, max1, max2
            elif num > max2:
                max2, max3 = num, max2
            elif num > max3:
                max3 = num
        if min2 >= 0 or max1 < 0:
            return max1 * max2 * max3
        else:
            if min1 * min2 > max2 * max3:
                return min1 * min2 * max1
            else:
                return max1 * max2 * max3

# Alternative solution

class Solution3:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])
