class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        output = 0
        for i in range(2, len(nums)):
            left = 0
            right = i - 1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    output += right - left
                    right -= 1
                else:
                    left += 1
        return output

# Alternative solution (Brute Force which gives TLE error)

class Solution1:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        output = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[k] >= nums[i] + nums[j]:
                        break
                    else:
                        output += 1
        return output
