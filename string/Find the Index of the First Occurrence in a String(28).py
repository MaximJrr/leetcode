def strStr(haystack: str, needle: str) -> int:
    if needle == "":
        return 0

    if needle in haystack:
        return haystack.index(needle)
    return -1


print(strStr(haystack = "leetcode", needle = "leeto"))
