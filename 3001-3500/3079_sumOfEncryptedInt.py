class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        total = 0

        for num in nums:
            num_str = str(num)
            length = len(num_str)
            max_num = "0"

            for char in num_str:
                if char > max_num:
                    max_num = char

            modified_num = max_num * length
            total += int(modified_num)

        return total
