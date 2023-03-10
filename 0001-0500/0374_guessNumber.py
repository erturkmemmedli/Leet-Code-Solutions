# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        return self.binarysearch(1, n)
        
    def binarysearch(self, start, end):
        mid = (start + end) // 2
        if guess(mid) == -1:
            return self.binarysearch(start, mid - 1)
        elif guess(mid) == 1:
            return self.binarysearch(mid + 1, end)
        elif guess(mid) == 0:
            return mid
