class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        set_nums = set(nums)
        set_all_nums = set(range(1, len(nums) + 1))
        return list(set_all_nums - set_nums)