class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        while left < right:
            mid = (left + right) // 2
            day_needed = 1
            current_cargo_weight = 0
            for weight in weights:
                if weight + current_cargo_weight > mid:
                    day_needed += 1
                    current_cargo_weight = 0
                current_cargo_weight += weight
            if day_needed > days:
                left = mid + 1
            else:
                right = mid
        return left
