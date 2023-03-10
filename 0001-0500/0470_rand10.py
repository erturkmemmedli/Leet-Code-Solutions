# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        result = (rand7() - 1) * 7 + rand7() - 1
        return result % 10 + 1 if result < 40 else self.rand10()
