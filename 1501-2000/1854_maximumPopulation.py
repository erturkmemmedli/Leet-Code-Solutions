class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        years = []
        for b, d in logs:
            years.append([b, 1])
            years.append([d-1, -1])
        years.sort(key=lambda x: [x[0], -x[1]])

        max_pop = 0
        curr_sum = 0
        res_year = 0
        for y, x in years:
            curr_sum += x
            if curr_sum > max_pop:
                max_pop = curr_sum
                res_year = y
        return res_year
