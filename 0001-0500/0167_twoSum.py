class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while numbers[i] + numbers[j] != target:
            if numbers[i] + numbers[j] > target:
                j -= 1
            if numbers[i] + numbers[j] < target:
                i += 1
        return [i+1, j+1]

# Alternative solution
    
class Solution1:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, number in enumerate(numbers):
            if number not in hashmap:
                hashmap[target-number] = i + 1
            else:
                return [hashmap[number], i + 1]

# Alternative solution

class Solution2:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            val = target - numbers[i]
            left, right = i+1, n-1
            while left <= right:
                mid = (left+right) // 2
                if numbers[mid] == val:
                    return [i+1, mid+1]
                if numbers[mid] > val:
                    right = mid-1
                if numbers[mid] < val:
                    left = mid+1

# Alternative solution

class Solution:
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return left + 1, right + 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
