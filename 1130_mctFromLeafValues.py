class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        summ = 0
        while len(arr) > 1:
            index = arr.index(min(arr))
            if index == 0:
                summ += arr[index] * arr[index+1]
            elif index == len(arr)-1:
                summ += arr[index] * arr[index-1]
            else:
                summ += arr[index] * min(arr[index-1],arr[index+1])
            arr.pop(index)
        return summ
      
# Alternative solution

class Solution1:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        stack = [float('INF')]
        total = 0
        for val in arr:
            while stack[-1] < val:
                total += stack.pop() * min(val, stack[-1])
            stack.append(val)
        while len(stack) > 2:
            total += stack.pop() * stack[-1]
        return total

# Alternative solution  

class Solution2:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        return self.dynamic_programming(arr, 0, len(arr), {})
        
    def dynamic_programming(self, arr, i, j, memo):
        if i + 1 == j:
            return 0
        if (i,j) not in memo:
            result = float('INF')
            for k in range(i+1, j):
                root = max(arr[i:k]) * max(arr[k:j])
                left = self.dynamic_programming(arr, i, k, memo)
                right = self.dynamic_programming(arr, k, j, memo)
                total = left + root + right
                result = min(result, total)
            memo[(i,j)] = result
        return memo[(i,j)]
