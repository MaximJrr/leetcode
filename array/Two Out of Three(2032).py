import collections


def twoOutOfThree(nums1: list[int], nums2: list[int], nums3: list[int]) -> list[int]:
    intersection_1 = set(nums1).intersection(set(nums2))
    intersection_2 = set(nums2).intersection(set(nums3))
    intersection_3 = set(nums1).intersection(set(nums3))
    return list(set(list(intersection_1) + list(intersection_2) + list(intersection_3)))


if __name__ == '__main__':
    print(twoOutOfThree(nums1 = [3,1], nums2 = [2,3], nums3 = [1,2]))