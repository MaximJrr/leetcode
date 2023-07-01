def maxRepeating(sequence: str, word: str) -> int:
    split_sequence = sequence.replace(word, '##')
    pointer = 0
    count = 0

    while pointer < len(split_sequence):
        if split_sequence[pointer] == '#':
            count += 1
            pointer += 1
        else:
            pointer += 1

    return count


print(maxRepeating("aaabaaaabaaabaaaabaaaabaaaabaaaaba", word = "aaaba"))