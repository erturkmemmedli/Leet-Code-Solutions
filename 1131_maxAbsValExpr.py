class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        case1, case2, case3, case4 = [], [], [], []
        for i in range(len(arr1)):
            case1.append(arr1[i] - arr2[i] + i)
            case2.append(arr1[i] + arr2[i] + i)
            case3.append(-arr1[i] - arr2[i] + i)
            case4.append(-arr1[i] + arr2[i] + i)
        maximum = max(max(case1) - min(case1),
                      max(case2) - min(case2),
                      max(case3) - min(case3),
                      max(case4) - min(case4))
        return maximum
