class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i, j, count = 0, len(people) - 1, 0
        while i <= j:
            if i == j:
                count += 1
                i += 1
            elif people[j] + people[i] <= limit:
                count += 1
                i += 1
                j -= 1
            else:
                count += 1
                j -= 1
        return count
