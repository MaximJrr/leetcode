class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing_count = 0
        pointer = 0
        current = 1

        while missing_count < k:
            if pointer < len(arr) and arr[pointer] == current:
                pointer += 1
            else:
                missing_count += 1
                if missing_count == k:
                    return current
            current += 1

        return -1
