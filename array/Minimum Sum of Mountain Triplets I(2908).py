def minimumSum(nums):
    nums_lst = []

    for num in range(1, len(nums) - 1):
        if nums[num] > nums[num - 1] and nums[num] > nums[num + 1]:
            nums_lst.append(nums[num] + nums[num - 1] + nums[num + 1])

    if nums_lst:
        return min(nums_lst)
    return - 1


if __name__ == '__main__':
    print(minimumSum(nums = [6,5,4,3,4,5]))
