from collections import Counter


def duplicateNumbersXOR(nums: list[int]) -> int:
    counts = Counter(nums)
    result = 0

    for i, j in counts.items():
        if j == 2:
            result ^= i

    return result


print(duplicateNumbersXOR([1,2,1,3]))

