class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        result = [(a - b, a, b) for a, b in costs]
        result.sort()
        answer = 0
        for i in range(len(costs)//2):
            answer += result[i][1]
        for j in range(len(costs)//2, len(costs)):
            answer += result[j][2]
        return answer
