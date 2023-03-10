class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hand.sort()
        queue = collections.deque()
        for num in hand:
            if not queue:
                queue.append([num])
            else:
                i = 0
                while i < len(queue) and queue[i][-1] == num:
                    i += 1
                if i == len(queue):
                    queue.append([num])
                elif queue[i][-1] + 1 == num:
                    queue[i].append(num)
                else:
                    return False
            if len(queue[0]) == groupSize:
                queue.popleft()
        return not queue
