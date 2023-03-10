class Solution:
    def printVertically(self, s: str) -> List[str]:
        stringList = s.split()
        length = len(max(stringList, key = len))
        finalList = []
        for word in stringList:
            finalList.append([char for char in word])
            finalList[-1] += [" "] * (length - len(word))
        transposeList = list(zip(*finalList))
        answerList = []
        for letters in transposeList:
            answerList.append("".join(letters).rstrip())
        return answerList
