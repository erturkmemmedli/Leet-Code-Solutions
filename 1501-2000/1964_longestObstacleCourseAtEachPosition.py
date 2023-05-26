class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        lengths = []
        longest_increasing_subsequence = []

        for obstacle in obstacles:
            index = self.binary_search(longest_increasing_subsequence, obstacle)

            if index == len(longest_increasing_subsequence):
                longest_increasing_subsequence.append(obstacle)

            else:
                longest_increasing_subsequence[index] = obstacle
                
            lengths.append(index + 1)

        return lengths


    def binary_search(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] <= target:
                left = mid + 1

            else:
                right = mid - 1

        return left
