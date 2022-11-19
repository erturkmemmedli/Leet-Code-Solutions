class Solution:
    def maxOperations(self, nums, k):
        hashmap = {}
        operation = 0
        for i in range(len(nums)):
            if nums[i] >= k:
                continue
            if nums[i] not in hashmap:
                if k - nums[i] not in hashmap:
                    hashmap[k - nums[i]] = [i]
                else:
                    hashmap[k - nums[i]].append(i)
            else:
                hashmap[nums[i]].pop()
                if hashmap[nums[i]] == []:
                    del(hashmap[nums[i]])
                operation += 1
        return operation
