class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        result = 0

        for num in nums:
            max_digit = max(str(num))
            encrypted_num = int(max_digit * len(str(num)))
            result += encrypted_num

        return result
