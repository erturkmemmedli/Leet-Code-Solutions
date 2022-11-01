class Solution:
    def maximumSwap(self, num: int) -> int:
        numList = []
        temp = num
        while temp:
            numList.append(temp % 10)
            temp //= 10
        compare = sorted(numList)
        i, find, index = len(numList) - 1, None, None
        while i >= 0:
            if numList[i] == compare[i]:
                i -= 1
            else:
                find = compare[i]
                index = i
                break
        if not find:
            return num
        for i in range(0, index):
            if numList[i] == find:
                numList[i], numList[index] = numList[index], numList[i]
                break
        answer = 0
        for i in range(len(numList) - 1, -1, -1):
            answer += numList[i] * 10 ** i
        return answer
