class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        calory = sum(calories[:k])
        point = 1 if calory > upper else -1 if calory < lower else 0
        for i in range(len(calories) - k):
            calory += calories[i + k] - calories[i]
            if calory > upper:
                point += 1
            elif calory < lower:
                point -= 1
        return point
