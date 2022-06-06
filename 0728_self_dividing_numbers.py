class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        output = []
        for i in range(left, right+1):
            div = i
            while div:
                if div % 10 == 0:
                    break
                if i % (div % 10) != 0:
                    break
                div = div // 10
            if div == 0:
                output.append(i)
        return output
