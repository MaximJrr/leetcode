def findDisappearedNumbers(nums):
    set_nums = set(nums)
    set_all_nums = set(range(1, len(nums) + 1))
    return list(set_all_nums - set_nums)

print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))

