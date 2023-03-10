class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        table, answer, index = [], 0, 0
        for i in range(len(difficulty)):
            table.append([difficulty[i], profit[i]])
        table.sort(key = lambda x: [-x[1], x[0]])
        worker.sort(reverse = True)
        for person in worker:
            while index < len(table) and person < table[index][0]:
                index += 1
            if index == len(table):
                break
            answer += table[index][1]
        return answer
