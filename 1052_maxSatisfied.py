class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        max_customer = 0
        temp = 0
        tracking_indexes = deque()
        how_much_left = minutes
        total = sum([customers[i] for i in range(n) if grumpy[i] == 0])
        window = collections.deque()
        for i in range(n):
            if not tracking_indexes and (not window or window[-1][1] != 1):
                window.append((customers[i], grumpy[i]))
                temp += customers[i]
                if grumpy[i] == 1:
                    tracking_indexes.append(i)
                    how_much_left -= 1
                else:
                    total -= customers[i]
                max_customer = max(max_customer, temp + total)
                continue
            if grumpy[i] == 1:
                if how_much_left and i - tracking_indexes[0] < minutes:
                    how_much_left -= 1
                    window.append((customers[i], grumpy[i]))
                    temp += customers[i]
                    max_customer = max(max_customer, temp + total)
                    tracking_indexes.append(i)
                else:
                    while tracking_indexes and i - tracking_indexes[0] >= minutes:
                        while window[0][1] == 0:
                            cus, gru = window.popleft()
                            total += cus 
                            temp -= cus
                        temp -= window.popleft()[0]
                        tracking_indexes.popleft()
                    window.append((customers[i], grumpy[i]))
                    tracking_indexes.append(i)
                    temp += customers[i]
                    max_customer = max(max_customer, temp + total)
            else:
                window.append((customers[i], grumpy[i]))
                temp += customers[i]
                total -= customers[i]
                max_customer = max(max_customer, temp + total)
        return max_customer
