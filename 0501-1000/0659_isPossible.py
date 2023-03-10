class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        subsequences = []
        for num in nums:
            if not subsequences:
                subsequences.append([num])
                continue
            i = len(subsequences) - 1
            if num == subsequences[i][-1] + 1:
                subsequences[i].append(num)
            elif num == subsequences[i][-1]:
                flag = False
                while i > 0:
                    i -= 1
                    if num == subsequences[i][-1] + 1:
                        subsequences[i].append(num)
                        flag = True
                        break
                if not flag and i == 0:
                    subsequences.append([num])
            else:
                if len(subsequences[-1]) < 3:
                    return False
                subsequences.append([num])
        return all(len(seq) >= 3 for seq in subsequences)
