class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = [prices[-1]]
        discounts = [0]
        for i in range(len(prices)-2,-1,-1):
            if prices[i] < prices[i+1]:
                while stack and stack[-1] > prices[i]:
                    stack.pop()
                if stack:
                    discounts.append(stack[-1])
                    stack.append(prices[i])
                else:
                    discounts.append(0)
                    stack.append(prices[i])
            else:
                discounts.append(prices[i+1])
                stack.append(prices[i])
        discounts = discounts[::-1]
        return list([prices[i] - discounts[i] for i in range(len(prices))])
