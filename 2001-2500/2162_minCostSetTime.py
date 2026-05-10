class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        minute, second = divmod(targetSeconds, 60)

        def calculateCost(minute, second):
            minute_first, minute_second = divmod(minute, 10)
            second_first, second_second = divmod(second, 10)
            states = [second_second, second_first, minute_second, minute_first]
            while states and states[-1] == 0:
                states.pop()

            curr_state = startAt
            cost = 0
            while states:
                state = states.pop()
                if state != curr_state:
                    cost += moveCost
                    curr_state = state
                cost += pushCost
            
            return cost

        cost1 = calculateCost(minute, second) if minute < 100 else float('inf')
        cost2 = calculateCost(minute - 1, second + 60) if second + 60 <= 99 else float('inf')
        return min(cost1, cost2)
            
