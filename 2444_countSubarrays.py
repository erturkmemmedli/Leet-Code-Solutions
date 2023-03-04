class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count = 0
        minIndex, maxIndex, offset, equals = deque(), deque(), deque(), 0

        for i, num in enumerate(nums):
            if num == minK == maxK:
                equals += 1
            
            elif num == minK:
                minIndex.append(i)

            elif num == maxK:
                maxIndex.append(i)

            elif minK < num < maxK:
                offset.append(i)

            if num < minK or num > maxK or i == len(nums) - 1:
                while (minIndex and maxIndex) or equals:
                    if equals:
                        count += equals * (equals + 1) // 2
                        break
                    
                    elif min(minIndex[0], maxIndex[0], (offset[0] if offset else inf)) == minIndex[0]:
                        minIndex.popleft()
                        if minIndex:
                            count += max(minIndex[-1], maxIndex[-1], (offset[-1] if offset else -inf)) - maxIndex[0] + 1
                        else:
                            count += max(maxIndex[-1], (offset[-1] if offset else -inf)) - maxIndex[0] + 1

                    elif min(minIndex[0], maxIndex[0], (offset[0] if offset else inf)) == maxIndex[0]:
                        maxIndex.popleft()
                        if maxIndex:
                            count += max(minIndex[-1], maxIndex[-1], (offset[-1] if offset else -inf)) - minIndex[0] + 1
                        else:
                            count += max(minIndex[-1], (offset[-1] if offset else -inf)) - minIndex[0] + 1

                    elif min(minIndex[0], maxIndex[0], (offset[0] if offset else inf)) == offset[0]:
                        offset.popleft()
                        if offset:
                            count += max(minIndex[-1], maxIndex[-1], offset[-1]) - max(minIndex[0], maxIndex[0]) + 1
                        else:
                            count += max(minIndex[-1], maxIndex[-1]) - max(minIndex[0], maxIndex[0]) + 1

                minIndex, maxIndex, offset, equals = deque(), deque(), deque(), 0
                
        return count
