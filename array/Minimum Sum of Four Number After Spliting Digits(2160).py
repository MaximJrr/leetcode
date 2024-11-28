def minimumSum(num: int) -> int:
    result = []
    left_pointer = 0
    right_pointer = 2
    sorted_num = sorted(' '.join(str(num)).split())

    while right_pointer < len(sorted_num):
        result.append(int(sorted_num[left_pointer] + sorted_num[right_pointer]))
        left_pointer += 1
        right_pointer += 1

    return sum(result)




print(minimumSum(4009))
