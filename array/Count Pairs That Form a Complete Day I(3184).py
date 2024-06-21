def countCompleteDayPairs(hours: list[int]) -> int:
    counter = 0

    for i in range(len(hours)):
        for j in range(i + 1, len(hours)):
            if (hours[i] + hours[j]) % 24 == 0:
                counter += 1

    return counter
