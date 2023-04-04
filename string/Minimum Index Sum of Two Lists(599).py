def findRestaurant(list1, list2):
    hash_list1 = {}
    result = []

    for index, word in enumerate(list1):
        if word not in list2:
            continue
        if word in list2:
            hash_list1[word] = index

    for index, word in enumerate(list2):
        if word not in list1:
            continue
        if word in list1:
            hash_list1[word] += index

    min_value = min(hash_list1.values())

    for word in hash_list1:
        if hash_list1[word] == min_value:
            result.append(word)
    return result[::-1]



print(findRestaurant(list1 = ["happy","sad","good"], list2 = ["sad","happy","good"]))
