class Solution:
    def largestInteger(self, num: int) -> int:
        num_str = str(num)
        even = deque()
        odd = deque()
        counter = sorted(Counter(num_str).most_common(), reverse=True)
        result = [None] * len(num_str)

        for i, val in enumerate(num_str):
            if int(val) % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        
        for val, cnt in counter:
            int_val = int(val)
            for _ in range(cnt):
                if int_val % 2 == 0:
                    idx = even.popleft()
                    result[idx] = val
                else:
                    idx = odd.popleft()
                    result[idx] = val
            
        return int("".join(result))
        
