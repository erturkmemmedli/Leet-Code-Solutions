class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = collections.Counter(nums)
        result = []
        n = len(nums) // 3
        for key, val in c.items():
            if val > n:
                result.append(key)
        return result

# Alternative solution

class Solution1:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Boyer-Moore Majority Vote algorithm
        candidate1, candidate2, count1, count2 = 1, 0, 0, 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2 :
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1, count2 = count1 - 1, count2 - 1
        result = []
        if nums.count(candidate1) > len(nums) // 3:
            result.append(candidate1)
        if nums.count(candidate2) > len(nums) // 3:
            result.append(candidate2)
        return result
