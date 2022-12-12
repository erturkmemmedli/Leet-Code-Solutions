class Solution:
    def nextGreaterElement(self, n: int) -> int:
        number = list(map(int, str(n)))
        pivot = None
        for i in range(len(number) - 1):
            if number[i] < number[i + 1]:
                pivot = i
        if pivot == None: return -1
        small = pivot + 1
        for i in range(pivot + 1, len(number)):
            if number[pivot] < number[i] < number[small]:
                small = i
        number[pivot], number[small] = number[small], number[pivot]
        following = sorted(number[pivot + 1:], reverse = True)
        for i in range(pivot + 1, len(number)):
            number[i] = following.pop()
        result = 0
        for i in range(len(number) - 1, -1, -1):
            result += number[i] * 10 ** (len(number) - i - 1)
        return result if result < 2 ** 31 else -1
