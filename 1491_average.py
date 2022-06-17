class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        return sum(salary[1:len(salary)-1]) / (len(salary)-2)
      
# Alternative solution

class Solution:
    def average(self, salary: List[int]) -> float:
        return (sum(salary) - min(salary) - max(salary)) / (len(salary) - 2)
