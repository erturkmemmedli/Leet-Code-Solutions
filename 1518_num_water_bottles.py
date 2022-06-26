class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result = numBottles
        while numBottles // numExchange > 0:
            add = numBottles // numExchange
            remain = numBottles % numExchange
            result += add
            numBottles = add + remain
        return result
      
# Alternative solution

class Solution1:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return numBottles + self.calculate(numBottles, numExchange)
    
    def calculate(self, bot, ex):
        if bot < ex: return 0
        return bot // ex + self.calculate(bot // ex + bot % ex, ex)
