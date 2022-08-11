class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList: return []
        answer = []
        i, j = 0, 0
        while i < len(firstList) and j < len(secondList):
            if firstList[i][1] < secondList[j][0]:
                i += 1
                continue
            if secondList[j][1] < firstList[i][0]:
                j += 1
                continue
            answer.append([max(firstList[i][0], secondList[j][0]), min(firstList[i][1], secondList[j][1])])
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        return answer
